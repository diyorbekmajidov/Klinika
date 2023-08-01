from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # my apps
    path("klinika/", include("klinika.urls")),
    path("user/", include("user.urls")),
]
