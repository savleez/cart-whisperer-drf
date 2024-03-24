from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import CategoryViewSet


router_v1 = DefaultRouter()
router_v1.register(prefix=r"category", viewset=CategoryViewSet, basename="category")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
