from network.apps import NetworkConfig
from rest_framework.routers import DefaultRouter

from network.views import NetworkViewSet

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r"networks", NetworkViewSet, basename="networks")

urlpatterns = [] + router.urls
