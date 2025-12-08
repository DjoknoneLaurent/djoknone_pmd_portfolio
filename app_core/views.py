from django.shortcuts import render
from .models import Profile
from app_skills.models import SkillCategory
from app_projects.models import Project
from app_experience.models import Experience, Education


def index(request):
    """Page d'accueil du portfolio"""
    context = {
        'profile': Profile.objects.first(),
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all(),
        'featured_projects': Project.objects.filter(is_featured=True)[:3],
        'experiences': Experience.objects.all()[:3],
        'educations': Education.objects.all()[:3],
    }
    return render(request, 'app_core/home.html', context)