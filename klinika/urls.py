from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import *

router = DefaultRouter()

urlpatterns = [
    path("klinika/", KlinikaApiview.as_view()),
    path("xizmatlar/", XizmatlarApiview.as_view()),
    path("xizmatlar/<int:pk>/", XizmatlarGet.as_view()),
    path("shifokorlar/", ShifokorlarApiview.as_view()),
    path("narxlar/", NarxlarApiview.as_view()),
    path("narxlar/<int:pk>/", NarxlarGet.as_view()),
    path("shifokor/<int:pk>/", ShifokorGet.as_view()),
    path("navbatlar/", NavbatApiview.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)