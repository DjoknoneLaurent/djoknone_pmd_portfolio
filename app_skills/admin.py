from django.contrib import admin
from .models import SkillCategory, Skill


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'order')
    list_filter = ('category', 'level')
    list_editable = ('order',)
    search_fields = ('name',)
    ordering = ('category', 'order')