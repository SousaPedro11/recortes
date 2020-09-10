from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'recortesdiario', views.RecortesDiarioViewSet)
router.register(r'recorteslinkignorado', views.RecortesLinkIgnoradoViewSet)
router.register(r'recortesmonitoradownloads', views.RecortesMonitoradownloadsViewSet)
router.register(r'recortesnumeracaoerrada', views.RecortesNumeracaoErradaViewSet)
router.register(r'recortesrecorte', views.RecortesRecorteViewSet)
router.register(r'recortesrecortestfstj', views.RecortesRecorteStfStjViewSet)
router.register(r'recortesrecortetjmt', views.RecortesRecorteTjmtViewSet)

urlpatterns = router.urls
