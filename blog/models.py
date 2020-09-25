from django.db import models
from genoskul.common.timestamp import TimeStampModel
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from tinymce_4.fields import TinyMCEModelField


User = get_user_model()


class PostCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nom')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(TimeStampModel):
    title = models.CharField(max_length=100, verbose_name="Titre de l'article")
    slug = models.SlugField()
    content = TinyMCEModelField(verbose_name="Contenu")
    image = models.ImageField(
        verbose_name='Image de couverture', upload_to='posts/', blank=True, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    # publish = models.BooleanField(default=False, verbose_name="publier")
    category = models.ForeignKey(
        PostCategory, related_name='posts', null=True ,on_delete=models.CASCADE, verbose_name='Categorie')

    # objects = PostManager()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def get_absolute_url(self):
        return reverse("blog:post-details", kwargs={"slug": self.slug})


class Comment(TimeStampModel):
    content = models.TextField(verbose_name='Contenu du commentaire')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             verbose_name='Article', related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Utilisateur', related_name='comments')

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        return self.content[:30]
