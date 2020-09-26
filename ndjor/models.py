from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from genoskul.common.timestamp import TimeStampModel


User = get_user_model()


class ProductManager(models.Manager):
    def get_products(self, query=None):
        qs = self.get_queryset()
        if query:
            return qs.filter(
                Q(name__icontains=query) |
                Q(state__icontains=query) |
                Q(reference__icontains=query) |
                Q(location__icontains=query) |
                Q(price__icontains=query)
            )

        return qs



class ProductCategory(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name='Nom de la catégorie')

    def __str__(self):
        return self.name


class Product(TimeStampModel):
    name = models.CharField(max_length=100, verbose_name='Nom du produit')
    state = models.CharField(max_length=30, choices=(
        ('new', 'Neuf'), ('like_new', 'Comme Neuf'), ('others', 'Autres')), verbose_name='Etat du produit')
    categories = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, verbose_name='Catégorie du produit', related_name='products')
    reference = models.CharField(
        max_length=254, verbose_name='Contact du vendeur')
    image = models.ImageField(verbose_name='Photo de produit', blank=False, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products', verbose_name='Propriétaire')
    location = models.CharField(max_length=30, verbose_name='Lieu de vente')
    price = models.CharField(max_length=30, blank=True, verbose_name='Prix')

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
