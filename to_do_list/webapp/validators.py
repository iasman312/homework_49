from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


def prohibited_word(string):
    if 'apple' in string:
        raise ValidationError('There is a prohibited word')



