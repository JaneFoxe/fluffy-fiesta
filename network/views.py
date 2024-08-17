from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import Network
from network.permissions import IsActiveEmployee
from network.serializers import NetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["contact__country"]
    permission_classes = [IsActiveEmployee]
