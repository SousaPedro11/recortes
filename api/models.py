# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'django_migrations'
# The error was: permission denied for relation django_migrations
# Unable to inspect table 'recortes_controle'
# The error was: permission denied for relation recortes_controle


class RecortesDiario(models.Model):
    data_criacao = models.DateField()
    data_modificacao = models.DateTimeField(blank=True, null=True)
    data_publicacao = models.DateTimeField()
    codigo_diario = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'recortes_diario'
# Unable to inspect table 'recortes_downloaddiario'
# The error was: permission denied for relation recortes_downloaddiario


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
        managed = False
        db_table = 'recortes_link_ignorado'
# Unable to inspect table 'recortes_logcommanddownload'
# The error was: permission denied for relation recortes_logcommanddownload


class RecortesMonitoradownloads(models.Model):
    data = models.DateField()
    diario = models.CharField(max_length=200)
    hora_inicial = models.DateTimeField()
    hora_final = models.DateTimeField()
    quantidade = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'recortes_monitoradownloads'
# Unable to inspect table 'recortes_nomecaderno'
# The error was: permission denied for relation recortes_nomecaderno
# Unable to inspect table 'recortes_nomediario'
# The error was: permission denied for relation recortes_nomediario
# Unable to inspect table 'recortes_nomediario_20191024'
# The error was: permission denied for relation recortes_nomediario_20191024


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
        managed = False
        db_table = 'recortes_recorte_tjmt'
# Unable to inspect table 'recortes_registrodownloaddiario'
# The error was: permission denied for relation recortes_registrodownloaddiario
