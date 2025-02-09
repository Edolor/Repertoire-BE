from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HealthCheckView

urlpatterns = [
    path('', HealthCheckView.as_view(), name="health"),
    path('admin/GbxdJqi93laTCPC/', admin.site.urls),
    path('projects/', include("project.urls")),
    path('contact/', include("contact.urls")),
    path('about/', include("about.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
