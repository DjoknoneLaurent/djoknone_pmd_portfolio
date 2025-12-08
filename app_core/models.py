from django.db import models


class Profile(models.Model):
    """Informations personnelles du propriétaire du portfolio"""
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    headline = models.CharField(
        max_length=200,
        verbose_name="Titre professionnel",
        help_text="Ex: Statisticien | Data Analyst | Développeur Python"
    )
    bio = models.TextField(
        verbose_name="Biographie",
        help_text="Présentation détaillée (Markdown supporté)"
    )
    photo = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True,
        verbose_name="Photo de profil"
    )
    email = models.EmailField(verbose_name="Email de contact")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    location = models.CharField(max_length=100, blank=True, verbose_name="Localisation")
    
    # Réseaux sociaux
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn")
    github_url = models.URLField(blank=True, verbose_name="GitHub")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter/X")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    website_url = models.URLField(blank=True, verbose_name="Site web personnel")
    
    # CV téléchargeable
    cv_file = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        verbose_name="CV (PDF)"
    )
    
    # Meta
    is_available = models.BooleanField(
        default=True,
        verbose_name="Disponible pour opportunités",
        help_text="Affiche un badge 'Disponible' sur le site"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"