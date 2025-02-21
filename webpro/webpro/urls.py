from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('', include('cms.urls')),  # This will handle the homepage and other CMS pages
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 