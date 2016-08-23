from django.db import models
from app_projeto_ipc.models import *
from perfis.models import *
from django.contrib.auth.models import *

class estabelecimento(models.Model):
    NomeDoEstabeleciemento = models.CharField(max_length=150)
    Bairro                 = models.CharField(max_length=150)
    Rua                    = models.CharField(max_length=150)
    TeleFone               = models.CharField(max_length=150, blank=True)
    Email                  = models.EmailField(blank=True)
    usuario                = models.ForeignKey(User)

    def __unicode__(self):
        return self.NomeDoEstabeleciemento

    class Meta:
        verbose_name_plural = "Estabelecimento"
        db_table = "estabalecimento"

class rota(models.Model):
    Local_vizitar        = models.ForeignKey(estabelecimento)
    Pesquisador          = models.ForeignKey(perfil)
    data_vizita          = models.DateField()
    grupo__para_pesquisa = models.ForeignKey(pesos_grupos)
    SubGrupoParaPesquisa = models.ForeignKey(subgrupo)
    Item_pesquisado      = models.ForeignKey(item)
    usuario              = models.ForeignKey(User)

    def __unicode__(self):
        return self.Local_vizitar

    class Meta:
        verbose_name_plural = "Rota da pesquisa"
