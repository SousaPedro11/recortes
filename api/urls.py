from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

# router.register(r'diario', views.RecortesDiarioViewSet)
# router.register(r'linkignorado', views.RecortesLinkIgnoradoViewSet)
# router.register(r'monitoradownloads', views.RecortesMonitoradownloadsViewSet)
# router.register(r'numeracaoerrada', views.RecortesNumeracaoErradaViewSet)
router.register(r'recortes', views.RecortesRecorteViewSet)
# router.register(r'recortestfstj', views.RecortesRecorteStfStjViewSet)
# router.register(r'recortetjmt', views.RecortesRecorteTjmtViewSet)
router.register(r'tribunais', views.RecortesTribunaisViewset)

urlpatterns = router.urls
