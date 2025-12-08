from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'headline', 'email', 'is_available', 'updated_at')
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'headline', 'photo', 'bio')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Réseaux sociaux', {
            'fields': ('linkedin_url', 'github_url', 'twitter_url', 'facebook_url', 'website_url'),
            'classes': ('collapse',)
        }),
        ('Documents', {
            'fields': ('cv_file',)
        }),
        ('Statut', {
            'fields': ('is_available',)
        }),
    )

    def has_add_permission(self, request):
        # Empêche la création de plusieurs profils
        if Profile.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Empêche la suppression du profil
        return False