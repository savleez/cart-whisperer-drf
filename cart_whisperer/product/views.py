from rest_framework import viewsets
from rest_framework.response import Response

from product.models import Category
from product.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """Simple Viewset for viewing and editing categories."""

    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
