from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from genoskul.common.timestamp import TimeStampModel

User = get_user_model()


class DocumentCategory(TimeStampModel):
    name = models.CharField(max_length=150, verbose_name='Nom')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Catégorie de document'
        verbose_name_plural = 'Catégories de document'

class DocumentType(TimeStampModel):
    name = models.CharField(max_length=100, verbose_name='Nom')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type de document'
        verbose_name_plural = 'Types de documents'


class Document(TimeStampModel):
    name = models.CharField(max_length=150, verbose_name='Nom', blank=True)
    file = models.FileField(verbose_name='Fichier')
    type = models.ForeignKey(
        DocumentType,
        verbose_name='Type du fichier', on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        DocumentCategory, blank=True, verbose_name='Catégories',
        help_text='Appuyez sur «Ctrl» pour sélectionner plusieurs')
    description = models.TextField(
        blank=True, verbose_name='Petite description')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documents', verbose_name='Créateur')
    download_count = models.IntegerField(
        blank=True, default=0, verbose_name='Nombre de téléchargements')

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name


def post_save_document_split_name(sender, instance, created, **kwargs):
    if created:
        file = instance.file
        instance.name = str(file).split('.')[0]
        instance.save()


post_save.connect(post_save_document_split_name, sender=Document)
