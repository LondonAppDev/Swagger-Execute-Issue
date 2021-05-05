"""
Sample view and serializers.
"""
from rest_framework import (
    serializers,
    viewsets,
    response,
)

from sample import models


class SampleSerializer(serializers.ModelSerializer):
    """Sample serializer to demonstrate issue."""

    class Meta:
        model = models.SampleModel
        fields = ['id', 'description']
        read_only_fields = ['id']


class SampleViewSet(viewsets.ModelViewSet):
    """Sample viewset."""
    serializer_class = SampleSerializer
    queryset = models.SampleModel.objects.all()
