from django.contrib import admin
from .models import Experience, Certification, Education


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'type', 'start_date', 'end_date', 'is_current')
    list_filter = ('type', 'is_current')
    search_fields = ('title', 'company')
    ordering = ('-start_date',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date', 'expiry_date')
    list_filter = ('issuer',)
    search_fields = ('name', 'issuer')
    ordering = ('-issue_date',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current',)
    search_fields = ('degree', 'institution', 'field_of_study')
    ordering = ('-start_date',)