from rest_framework import routers

from django.urls import path, include

from .views import PetViewSet


router = routers.DefaultRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
