from django.shortcuts import render, get_object_or_404
from .models import Project, Technology


def project_list(request):
    """Liste de tous les projets"""
    projects = Project.objects.exclude(status='archived').prefetch_related('technologies')
    technologies = Technology.objects.all()
    
    # Filtrage par technologie (optionnel)
    tech_slug = request.GET.get('tech')
    if tech_slug:
        projects = projects.filter(technologies__slug=tech_slug)
    
    context = {
        'projects': projects,
        'technologies': technologies,
        'current_tech': tech_slug,
    }
    return render(request, 'app_projects/project_list.html', context)


def project_detail(request, slug):
    """Détail d'un projet"""
    project = get_object_or_404(Project, slug=slug)
    
    # Projets similaires (même technologie)
    similar_projects = Project.objects.filter(
        technologies__in=project.technologies.all()
    ).exclude(id=project.id).distinct()[:3]
    
    context = {
        'project': project,
        'similar_projects': similar_projects,
    }
    return render(request, 'app_projects/project_detail.html', context)