from django.db import models


class RecortesDiario(models.Model):
    data_criacao = models.DateField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_diario'


class RecortesLinkIgnorado(models.Model):
    url = models.CharField(max_length=200)
    id_recorte = models.BigIntegerField()
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    motivo = models.TextField()
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=20)
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    remover_completamente = models.BooleanField()
    numeracao_unica = models.CharField(max_length=20)

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_link_ignorado'


class RecortesMonitoradownloads(models.Model):
    data = models.DateField()
    diario = models.CharField(max_length=200)
    hora_inicial = models.DateTimeField()
    hora_final = models.DateTimeField()
    quantidade = models.SmallIntegerField()

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_monitoradownloads'


class RecortesNumeracaoErrada(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)
    data_criacao = models.DateField(blank=True, null=True)
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=20, blank=True, null=True)
    recorte = models.TextField(blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    codigo_diario = models.CharField(max_length=200, blank=True, null=True)
    caderno = models.CharField(max_length=200, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    corrigido = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_numeracao_errada'


class RecortesRecorte(models.Model):
    data_criacao = models.DateField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=20)
    recorte = models.TextField()
    data_publicacao = models.DateField()
    codigo_diario = models.CharField(max_length=200)
    caderno = models.CharField(max_length=200, blank=True, null=True)
    novo_recorte = models.BooleanField()
    paginas_diario = models.TextField(blank=True, null=True)
    nup_invalido = models.BooleanField(blank=True, null=True)
    nup_invalido_msg = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_recorte'


class RecortesRecorteStfStj(models.Model):
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=20, blank=True, null=True)
    recorte = models.TextField()
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_recorte_stf_stj'


class RecortesRecorteTjmt(models.Model):
    data_criacao = models.DateTimeField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    numeracao_unica = models.CharField(max_length=40, blank=True, null=True)
    recorte = models.TextField()
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)
    caderno = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        app_label = 'api'
        managed = False
        db_table = 'recortes_recorte_tjmt'
