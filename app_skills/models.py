from django.db import models


class SkillCategory(models.Model):
    """Catégorie de compétences (ex: Langages, Frameworks, Outils, etc.)"""
    name = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Catégorie de compétence"
        verbose_name_plural = "Catégories de compétences"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Compétence individuelle"""
    LEVEL_CHOICES = [
        (1, 'Débutant'),
        (2, 'Intermédiaire'),
        (3, 'Avancé'),
        (4, 'Expert'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nom")
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills',
        verbose_name="Catégorie"
    )
    level = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES,
        default=2,
        verbose_name="Niveau"
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Classe d'icône (ex: fa-python, devicon-django-plain)",
        verbose_name="Icône"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"