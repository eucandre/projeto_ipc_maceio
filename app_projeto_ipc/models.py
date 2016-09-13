from django.db import models
from django.contrib.auth.models import *

GRUPOS = ((u'Aliemntacao_e_bebidas','Aliemntacao_e_bebidas'),(u'Habitacao','Habitacao'),(u'Artigos_e_residencia','Artigos_e_residencia'),
(u'Vestuario','Vestuario'),(u'Transportes','Transportes'),(u'Saude_e_cuidados_especiais','Saude_e_cuidados_especiais'),
(u'Despesas_pessoais','Despesas_pessoais'),(u'Educacao','Educacao'),(u'Comunicacao','Comunicao'))

VINCULO =  ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'))

class pesos_grupos(models.Model):
    '''
        A finalidade desta classe eh possibilitar a atribuicao dos pesos dos grupos, quando necessario a mudanca, sem a necessidade
    de mexer em linha de codigo e permitir que o administrador do projeto edite sem prejuizo ao sistema.
    '''

    grupo = models.CharField(choices=GRUPOS, max_length=150)
    peso = models.FloatField()
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.grupo

    class Meta:
        verbose_name_plural = "Pesos grupos"

class subgrupo(models.Model):
    '''
            Os subgrupos irao compor os grupos
    '''

    nome_subgrupo = models.CharField(max_length=150)
    peso_subgrupo = models.FloatField(verbose_name="peso do subgrupo")
    grupo_relacionado = models.ForeignKey(pesos_grupos)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_subgrupo

    class Meta:
        verbose_name_plural = "Subgrupos"


class item(models.Model):
    '''
        Este metodo cadastra o item e verifica se esta ativo
    '''
    nome_item = models.CharField(max_length=150)
    preco = models.FloatField()
    marca = models.CharField(max_length=150, blank=True)
    ativo = models.BooleanField()
    data_verificacao = models.DateField()
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_item

    class Meta:
        verbose_name_plural = "Item"

class subitem(models.Model):
    '''
        Cada subitem possui seu pesso, baseando-se na tabela da POF
    '''

    nome_subitem = models.CharField(max_length=150)
    peso_subitem = models.FloatField(verbose_name="peso do subitem")
    item_relacionado = models.ForeignKey(item)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_subitem

    class Meta:
        verbose_name_plural = "Subitem"

class perfil(models.Model):
    '''
        Esta classe tem a funcionalidade de cadastrar o perfil dos participantes do ipc para controlar as pesquisas realizadas.
    '''
    nome_pesquisador = models.CharField(max_length=150)
    vinculo = models.CharField(choices=VINCULO, max_length=150)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_pesquisador

class estabelecimento(models.Model):
    Nome = models.CharField(max_length=150)
    Bairro                 = models.CharField(max_length=150)
    Rua                    = models.CharField(max_length=150)
    TeleFone               = models.CharField(max_length=150, blank=True)
    Email                  = models.EmailField(blank=True)
    usuario                = models.ForeignKey(User)

    def __unicode__(self):
        return self.Nome

    class Meta:
        verbose_name_plural = "Estabelecimento"
        db_table = "estabalecimento"

class rota(models.Model):
    '''
        Seleciona a rota a ser seguida.
    '''
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
