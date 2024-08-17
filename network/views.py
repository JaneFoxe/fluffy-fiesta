from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import Network
from network.permissions import IsActiveEmployee
from network.serializers import NetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    """ViewSet для управления объектами модели Network
    Атрибуты:
        serializer_class (NetworkSerializer): Указывает сериализатор, который будет использоваться для преобразования
        данных в формате JSON и обратно.

        queryset (QuerySet): Определяет набор данных, с которым будет работать ViewSet. В данном случае это все объекты
        модели Network.

        filter_backends (tuple): Определяет бэкенды фильтрации, которые будут использоваться для фильтрации данных.
        Здесь используется `DjangoFilterBackend` для поддержки фильтрации на основе полей модели.

        filterset_fields (list): Указывает поля, по которым может выполняться фильтрация. В данном случае фильтрация
        возможна по полю `contact__country`.

        permission_classes (list): Определяет классы разрешений, которые будут применяться к этому ViewSet. Здесь
        используется `IsActiveEmployee`, что ограничивает доступ только для аутентифицированных и активных пользователей.
    """

    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["contact__country"]
    permission_classes = [IsActiveEmployee]
