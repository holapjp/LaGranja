from rest_framework import routers
from .viewsets import ClienteViewSet, AlimentacionViewSet, PorcinoViewSet

router = routers.SimpleRouter()
router.register("clientes",ClienteViewSet)
router.register("alimentaciones",AlimentacionViewSet)
router.register("porcinos",PorcinoViewSet)

urlpatterns = router.urls