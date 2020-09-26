from django.core.exceptions import ValidationError

def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('La taille du fichier ne doit pas dépasser 2 MB.')