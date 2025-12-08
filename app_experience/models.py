from django.db import models


class Experience(models.Model):
    """Expérience professionnelle"""
    TYPE_CHOICES = [
        ('work', 'Emploi'),
        ('internship', 'Stage'),
        ('freelance', 'Freelance'),
        ('volunteer', 'Bénévolat'),
    ]

    title = models.CharField(max_length=200, verbose_name="Poste")
    company = models.CharField(max_length=200, verbose_name="Entreprise / Organisation")
    company_url = models.URLField(blank=True, verbose_name="Site web de l'entreprise")
    location = models.CharField(max_length=100, blank=True, verbose_name="Lieu")
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='work',
        verbose_name="Type"
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Missions et réalisations (Markdown supporté)"
    )
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date de fin",
        help_text="Laisser vide si poste actuel"
    )
    is_current = models.BooleanField(default=False, verbose_name="Poste actuel")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"
        ordering = ['-is_current', '-start_date']

    def __str__(self):
        return f"{self.title} - {self.company}"


class Certification(models.Model):
    """Certification ou diplôme"""
    name = models.CharField(max_length=200, verbose_name="Nom de la certification")
    issuer = models.CharField(max_length=200, verbose_name="Organisme émetteur")
    issuer_logo = models.ImageField(
        upload_to='certifications/',
        blank=True,
        null=True,
        verbose_name="Logo de l'organisme"
    )
    credential_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="ID de certification"
    )
    credential_url = models.URLField(
        blank=True,
        verbose_name="Lien de vérification"
    )
    issue_date = models.DateField(verbose_name="Date d'obtention")
    expiry_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date d'expiration",
        help_text="Laisser vide si pas d'expiration"
    )
    description = models.TextField(blank=True, verbose_name="Description")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.name} ({self.issuer})"


class Education(models.Model):
    """Formation académique"""
    degree = models.CharField(max_length=200, verbose_name="Diplôme")
    field_of_study = models.CharField(max_length=200, verbose_name="Domaine d'études")
    institution = models.CharField(max_length=200, verbose_name="Établissement")
    institution_url = models.URLField(blank=True, verbose_name="Site web de l'établissement")
    location = models.CharField(max_length=100, blank=True, verbose_name="Lieu")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date de fin",
        help_text="Laisser vide si en cours"
    )
    is_current = models.BooleanField(default=False, verbose_name="En cours")
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Détails sur la formation, mentions, etc."
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['-is_current', '-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"