from datetime import datetime
from functools import reduce
from operator import and_

from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.exceptions import ParseError
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import RecortesLinkIgnorado, RecortesMonitoradownloads, RecortesNumeracaoErrada, \
    RecortesRecorte, RecortesRecorteStfStj, RecortesRecorteTjmt, RecortesDiario
from api.serializers import RecortesDiarioSerializer, RecortesLinkIgnoradoSerializer, \
    RecortesMonitoradownloadsSerializer, RecortesNumeracaoErradaSerializer, RecortesRecorteSerializer, \
    RecortesRecorteStfStjSerializer, RecortesRecorteTjmtSerializer, RecortesTribunaisSerializer


class RecortesDiarioViewSet(ReadOnlyModelViewSet):
    queryset = RecortesDiario.objects.order_by('pk')
    serializer_class = RecortesDiarioSerializer

    def get_queryset(self):
        p = self.request.query_params.get('p')
        c = self.request.query_params.get('c')
        if p:
            try:
                p = datetime.strptime(p, '%d%m%Y')
                p = p.strftime("%Y-%m-%d")
            except ValueError:
                raise ParseError('Incorrect date format, should be ddmmyyy')
            self.queryset = self.queryset.filter(data_publicacao=p)

        if c:
            try:
                c = datetime.strptime(c, '%d%m%Y')
                c = c.strftime("%Y-%m-%d")
            except ValueError:
                raise ParseError('Incorrect date format, should be ddmmyyy')
            self.queryset = self.queryset.filter(data_criacao=c)

        return self.queryset.all()


class RecortesLinkIgnoradoViewSet(ReadOnlyModelViewSet):
    queryset = RecortesLinkIgnorado.objects.order_by('pk')
    serializer_class = RecortesLinkIgnoradoSerializer


class RecortesMonitoradownloadsViewSet(ReadOnlyModelViewSet):
    queryset = RecortesMonitoradownloads.objects.order_by('pk')
    serializer_class = RecortesMonitoradownloadsSerializer


class RecortesNumeracaoErradaViewSet(ReadOnlyModelViewSet):
    queryset = RecortesNumeracaoErrada.objects.order_by('pk')
    serializer_class = RecortesNumeracaoErradaSerializer


class RecortesTribunaisViewset(ReadOnlyModelViewSet):
    queryset = RecortesRecorte.objects
    serializer_class = RecortesTribunaisSerializer

    @method_decorator(cache_page(60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        count = self.request.query_params.get('count').replace('[', '').replace(']', '')

        if count:
            self.queryset = self.queryset.filter(
                reduce(
                    and_, (
                        Q(codigo_diario__icontains=term.strip()) for term in count.split('-')
                    )
                )
            ).values('recorte')
            print(self.queryset.query)
            return self.queryset.count()

        self.queryset = self.queryset.filter(recorte__isnull=False).values('codigo_diario').distinct()
        print(self.queryset.query)
        return self.queryset


class RecortesRecorteViewSet(ReadOnlyModelViewSet):
    queryset = RecortesRecorte.objects
    serializer_class = RecortesRecorteSerializer

    @method_decorator(cache_page(60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        t = self.request.query_params.get('t')
        nup = self.request.query_params.get('nup')
        q = self.request.query_params.get('q').replace('[', '').replace(']', '')
        tj = self.request.query_params.get('tj')
        ttj = {}

        if nup:
            return self.queryset.filter(numeracao_unica=nup).all()

        if q:
            self.queryset = self.queryset.filter(
                reduce(
                    and_, (
                        Q(recorte__icontains=term.strip()) for term in q.split('-')
                    )
                )
            )
            return self.queryset.all()

        if t:
            try:
                t = datetime.strptime(t, '%d%m%Y')
                t = t.strftime("%Y-%m-%d")
                ttj['data_publicacao'] = t
            except ValueError:
                raise ParseError('Incorrect date format, should be ddmmyyy')

        if tj:
            ttj['codigo_diario'] = tj

        if ttj:
            return self.queryset.filter(**ttj).all()

        return self.queryset.all()


class RecortesRecorteStfStjViewSet(ReadOnlyModelViewSet):
    queryset = RecortesRecorteStfStj.objects.order_by('pk')
    serializer_class = RecortesRecorteStfStjSerializer


class RecortesRecorteTjmtViewSet(ReadOnlyModelViewSet):
    queryset = RecortesRecorteTjmt.objects.order_by('pk')
    serializer_class = RecortesRecorteTjmtSerializer
