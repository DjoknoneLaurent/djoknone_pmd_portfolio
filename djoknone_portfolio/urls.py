from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_core.urls')),
    path('skills/', include('app_skills.urls')),
    path('projects/', include('app_projects.urls')),
    path('experience/', include('app_experience.urls')),
    path('blog/', include('app_blog.urls')),
]

# Servir les fichiers media en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)