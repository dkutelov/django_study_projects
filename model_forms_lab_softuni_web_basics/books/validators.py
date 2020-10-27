from django.core.exceptions import ValidationError


def pages_validator(value):
    if value <= 0:
        raise ValidationError('Pages cannot be zero or negative')
