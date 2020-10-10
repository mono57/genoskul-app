from django.core.exceptions import ValidationError

def file_size(value):
    limit = 10 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('La taille du fichier ne doit pas dépasser 10 MB.')