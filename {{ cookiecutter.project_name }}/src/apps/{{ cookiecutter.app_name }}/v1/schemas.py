from marshmallow import Schema, fields, validates, ValidationError


class WelcomeSchema(Schema):
    """
    An example schema auto generated to validate fields.
    You can use Schema or using flask_marshmallow ModelSchema 
    if you work with SQLAlchemy
    """
    name = fields.String()

    @validates('name')
    def validate_name(self, name):
        """
        This serves only as example if you don't pass `require=True`
        as a parameters in the StringField
        Args:
            name: value to be validated
        Returns: value
        """
        if not name:
            raise ValidationError("The name cannot be empty")
        return name
