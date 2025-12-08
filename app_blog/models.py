from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Catégorie d'articles de blog"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name="Description")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Tag pour les articles"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(models.Model):
    """Article de blog scientifique"""
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
        ('archived', 'Archivé'),
    ]

    title = models.CharField(max_length=250, verbose_name="Titre")
    slug = models.SlugField(max_length=250, unique=True)
    excerpt = models.TextField(
        max_length=500,
        verbose_name="Extrait",
        help_text="Résumé de l'article (affiché dans les listes)"
    )
    content = models.TextField(
        verbose_name="Contenu",
        help_text="Contenu de l'article (Markdown et LaTeX supportés)"
    )
    cover_image = models.ImageField(
        upload_to='blog/covers/',
        blank=True,
        null=True,
        verbose_name="Image de couverture"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
        verbose_name="Catégorie"
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles',
        verbose_name="Tags"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name="Statut"
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name="Article vedette"
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Nombre de vues"
    )
    reading_time = models.PositiveSmallIntegerField(
        default=5,
        verbose_name="Temps de lecture (min)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    published_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Date de publication"
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-is_featured', '-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Calcul automatique du temps de lecture (~200 mots/minute)
        if self.content:
            word_count = len(self.content.split())
            self.reading_time = max(1, word_count // 200)
        super().save(*args, **kwargs)