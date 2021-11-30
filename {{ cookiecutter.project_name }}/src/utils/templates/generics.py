"""
Generics that can be used as template views and generics to manipulate HTML
REF: https://gist.github.com/tiagoarasilva
"""

from flask import abort
from flask import render_template
from flask import request
from flask.views import View


class ContextMixin(object):
    """
    A default context mixin that passes the keyword arguments received by
    get_context_data() as the template context.
    """
    extra_context = None

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class BaseView(ContextMixin, View):
    """
    Default base view for the use of the generics
    """
    template_name = None
    allowed_methods = ["get", "post", "head", "options", "delete", "put", "trace", "patch"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_methods = [m.lower() for m in self.allowed_methods]

    def get_template_name(self):
        return self.template_name

    def render_template(self, **context):
        return render_template(self.get_template_name(), **context)

    def render(self, *args, **kwargs):
        """Subclasses have to override this method to implement the
        actual view function code.  This method is called with all
        the arguments from the URL rule.
        """
        context = self.get_context_data(**kwargs)
        return self.render_template(**context)

    def dispatch_request(self, *args, **kwargs):
        method = getattr(self, request.method.lower(), None)

        # WE DONT WANT TO HANDLE WITH HEAD, SO WE RETRY WITH GET
        if method is None and request.method == "HEAD":
            method = getattr(self, "get", None)

        if not method:
            # RENDERS THE DEFAULT VIEW
            return self.render(**kwargs)

        if method and (request.method.lower() not in self.allowed_methods):
            abort(403, "Not allowed method %s" % request.method.upper())
        return method(*args, **kwargs)


class ListView(BaseView):
    """
    View representing a list of objects retrieved

    Renders a template and pass a list of objects

    Usage:
        `class MyListView(ListView):
            template_name = 'my_template.html'

            def get_queryset(self):
                return Users.query.all()

            def get_context_data(**kwargs):
                context = super().get_context_data(**kwargs)
                context.update({
                    ...
                })
                return context
        `
    """

    def get_queryset(self):
        raise NotImplementedError()

    def dispatch_request(self, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({
            'objects': self.get_queryset()
        })
        return self.render_template(**context)


class TemplateView(BaseView):
    """
    This replaces the main View from flask by using something more user friendly and visually
    more intuitive.

    Renders a template

    Usage:
        `class MyView(TemplateView):
            template_name = 'my_template.html'

            def get_context_data(**kwargs):
                context = super().get_context_data(**kwargs)
                context.update({
                    ...
                })
                return context
        `
    """
    pass
