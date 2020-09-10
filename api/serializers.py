from rest_framework.serializers import ModelSerializer
from api.models import RecortesDiario, RecortesLinkIgnorado, RecortesMonitoradownloads, RecortesNumeracaoErrada, RecortesRecorte, RecortesRecorteStfStj, RecortesRecorteTjmt


class RecortesDiarioSerializer(ModelSerializer):

    class Meta:
        model = RecortesDiario
        fields = '__all__'


class RecortesLinkIgnoradoSerializer(ModelSerializer):

    class Meta:
        model = RecortesLinkIgnorado
        fields = '__all__'


class RecortesMonitoradownloadsSerializer(ModelSerializer):

    class Meta:
        model = RecortesMonitoradownloads
        fields = '__all__'


class RecortesNumeracaoErradaSerializer(ModelSerializer):

    class Meta:
        model = RecortesNumeracaoErrada
        fields = '__all__'


class RecortesRecorteSerializer(ModelSerializer):

    class Meta:
        model = RecortesRecorte
        fields = '__all__'


class RecortesRecorteStfStjSerializer(ModelSerializer):

    class Meta:
        model = RecortesRecorteStfStj
        fields = '__all__'


class RecortesRecorteTjmtSerializer(ModelSerializer):

    class Meta:
        model = RecortesRecorteTjmt
        fields = '__all__'
