"""
All the generics to be used across the platform
"""
import typing as t

from flask.globals import current_app, request
from flask.typing import ResponseReturnValue
from flask.views import MethodView
from werkzeug.exceptions import BadRequest

from ..exceptions import DisallowedHost
from ..http import split_domain_and_port, validate_host


class HttpAllowed(MethodView):
    """Verifies the header of any request and checks if it's inside the allowed
    hosts settings.

    Returns 400 BAD REQUEST if not.
    """
    def get_port(self):
        """Return the port number for the request as a string."""
        if current_app.config['USE_X_FORWARDED_PORT'] and 'HTTP_X_FORWARDED_PORT' in request.environ:
            port = request.environ['HTTP_X_FORWARDED_PORT']
        else:
            port = request.environ['SERVER_PORT']
        return str(port)

    def _get_raw_host(self):
        """
        Return the HTTP host using the environment or request headers. Skip
        allowed hosts protection, so may return an insecure host.
        """
        # We try three options, in order of decreasing preference.
        if current_app.config['USE_X_FORWARDED_HOST'] and (
                'HTTP_X_FORWARDED_HOST' in request.environ):
            host = request.environ['HTTP_X_FORWARDED_HOST']
        elif 'HTTP_HOST' in request.environ:
            host = request.environ['HTTP_HOST']
        else:
            # Reconstruct the host using the algorithm from PEP 333.
            host = request.environ['SERVER_NAME']
            server_port = self.get_port()
            if server_port != ('443' if self.is_secure() else '80'):
                host = '%s:%s' % (host, server_port)
        return host

    def get_host(self):
        """Return the HTTP host using the environment or request headers."""
        host = self._get_raw_host()

        # ALLOWS VARIANTS OF LOCALHOST IF ALLOWED_HOSTS IS EMPTYy AND DEBUG=True.
        allowed_hosts = current_app.config['ALLOWED_HOSTS']
        if current_app.config['DEBUG'] and not allowed_hosts:
            allowed_hosts = ['.localhost', '127.0.0.1', '[::1]']

        domain, _ = split_domain_and_port(host)
        if domain and validate_host(domain, allowed_hosts):
            return host
        else:
            msg = "Invalid HTTP_HOST header: %r." % host
            if domain:
                msg += " You may need to add %r to ALLOWED_HOSTS." % domain
            else:
                msg += " The domain name provided is not valid according to RFC 1034/1035."
            raise DisallowedHost(msg)

    def dispatch_request(self, *args: t.Any, **kwargs: t.Any) -> ResponseReturnValue:
        try:
            self.get_host()
        except DisallowedHost as e:
            raise BadRequest(str(e))
        return super().dispatch_request(*args, **kwargs)
