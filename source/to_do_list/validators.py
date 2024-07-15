from django.core.exceptions import ValidationError

def summary_length(value):
    if len(value) < 10:
        raise ValidationError('Summary must be at least 10 characters long.')

def min_words(value):
    if len(value.split()) < 5:
        raise ValidationError('Description must be at least 5 words long.')