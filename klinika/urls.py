from urls import urlpatterns, path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("kilinikalar", KilinikarViewSet, basename="kilinikalar")