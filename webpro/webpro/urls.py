from django.urls import path, include

urlpatterns = [
    # ... other URL patterns ...
    path('', include('profiles.urls')),
] 