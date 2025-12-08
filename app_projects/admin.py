from django.contrib import admin
from .models import Technology, Project


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'order', 'created_at')
    list_filter = ('status', 'is_featured', 'technologies')
    list_editable = ('status', 'is_featured', 'order')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    date_hierarchy = 'created_at'