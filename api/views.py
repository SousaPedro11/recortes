from rest_framework.viewsets import ModelViewSet
from api.serializers import RecortesDiarioSerializer, RecortesLinkIgnoradoSerializer, RecortesMonitoradownloadsSerializer, RecortesNumeracaoErradaSerializer, RecortesRecorteSerializer, RecortesRecorteStfStjSerializer, RecortesRecorteTjmtSerializer
from api.models import RecortesDiario, RecortesLinkIgnorado, RecortesMonitoradownloads, RecortesNumeracaoErrada, RecortesRecorte, RecortesRecorteStfStj, RecortesRecorteTjmt


class RecortesDiarioViewSet(ModelViewSet):
    queryset = RecortesDiario.objects.order_by('pk')
    serializer_class = RecortesDiarioSerializer


class RecortesLinkIgnoradoViewSet(ModelViewSet):
    queryset = RecortesLinkIgnorado.objects.order_by('pk')
    serializer_class = RecortesLinkIgnoradoSerializer


class RecortesMonitoradownloadsViewSet(ModelViewSet):
    queryset = RecortesMonitoradownloads.objects.order_by('pk')
    serializer_class = RecortesMonitoradownloadsSerializer


class RecortesNumeracaoErradaViewSet(ModelViewSet):
    queryset = RecortesNumeracaoErrada.objects.order_by('pk')
    serializer_class = RecortesNumeracaoErradaSerializer


class RecortesRecorteViewSet(ModelViewSet):
    queryset = RecortesRecorte.objects.order_by('pk')
    serializer_class = RecortesRecorteSerializer


class RecortesRecorteStfStjViewSet(ModelViewSet):
    queryset = RecortesRecorteStfStj.objects.order_by('pk')
    serializer_class = RecortesRecorteStfStjSerializer


class RecortesRecorteTjmtViewSet(ModelViewSet):
    queryset = RecortesRecorteTjmt.objects.order_by('pk')
    serializer_class = RecortesRecorteTjmtSerializer
