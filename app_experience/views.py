from django.shortcuts import render
from .models import Experience, Education, Certification


def experience_list(request):
    """Page expériences, formations et certifications"""
    context = {
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
    }
    return render(request, 'app_experience/experience_list.html', context)