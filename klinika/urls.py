from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

urlpatterns = [
    path("klinika/", KlinikaApiview.as_view()),
    path("bulimlar/", BulimlarApiview.as_view()),
    path("shifokorlar/", ShifokorlarApiview.as_view()),
]