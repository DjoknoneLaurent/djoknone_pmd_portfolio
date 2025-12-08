from django.db import models


class Technology(models.Model):
    """Technologies utilisées dans les projets (pour le filtrage et les tags)"""
    name = models.CharField(max_length=50, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=50, unique=True)
    color = models.CharField(
        max_length=7,
        default="#6B7280",
        help_text="Couleur HEX (ex: #3B82F6)",
        verbose_name="Couleur"
    )

    class Meta:
        verbose_name = "Technologie"
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Projet du portfolio"""
    STATUS_CHOICES = [
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
        ('archived', 'Archivé'),
    ]

    title = models.CharField(max_length=200, verbose_name="Titre")
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(
        max_length=300,
        verbose_name="Description courte",
        help_text="Résumé en une ou deux phrases (affichée dans les cartes)"
    )
    description = models.TextField(
        verbose_name="Description complète",
        help_text="Description détaillée du projet (Markdown supporté)"
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name="Image de couverture"
    )
    technologies = models.ManyToManyField(
        Technology,
        related_name='projects',
        verbose_name="Technologies utilisées"
    )
    github_url = models.URLField(
        blank=True,
        verbose_name="Lien GitHub"
    )
    demo_url = models.URLField(
        blank=True,
        verbose_name="Lien Démo"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='completed',
        verbose_name="Statut"
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name="Projet vedette",
        help_text="Afficher en avant sur la page d'accueil"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-is_featured', 'order', '-created_at']

    def __str__(self):
        return self.title