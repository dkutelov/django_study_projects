from django.core.exceptions import ValidationError
import re


def validate_list_separated_by_comma_and_space(text):
    if ', ' not in text:
        raise ValidationError('Ingredients should be words separated by comma and space')

