from django.db import models
from django.contrib.auth.models import *

GRUPOS = ((u'1 - Aliemntacao_e_bebidas','1 - Aliemntacao_e_bebidas'),(u'2 - Habitacao','2 - Habitacao'),(u'3 - Artigos_e_residencia','3 - Artigos_e_residencia'),
(u'4 - Vestuario','4 - Vestuario'),(u'5 - Transportes','5 - Transportes'),(u'6 - Saude_e_cuidados_especiais','6 - Saude_e_cuidados_especiais'),
(u'7 - Despesas_pessoais','7 - Despesas_pessoais'),(u'8 - Educacao','8 - Educacao'),(u'9 - Comunicacao','9 - Comunicao'))

SUBGRUPOS = ((u'1.1 - Alimentacao_no_domicilio','1.1 - Alimentacao_no_domicilio'), (u'1.2 - Alimentacao_fora_do_domicilio','1.2 - Alimentacao_fora_do_domicilio'),
             (u'2.1 - Encargos_e_manutencao','2.1 - Encargos_e_manutencao'),(u'2.2 - Combustiveis_e_energia','2.2 - Combustiveis_e_energia'),
             (u'3.1 - Moveis_e_utensilios','3.1 - Moveis_e_utensilios'),(u'3.2 - Aparelhos_eletroeletronicos','3.2 - Aparelhos_eletroeletronicos'),
             (u'3.3 - Consertos_e_manutencao','3.3 - Consertos_e_manutencao'), (u'4.1 - Roupas','4.1 - Roupas'),(u'4.2 - Calcados_e_acessorios',''),
             (u'4.3 - Joias_e_bijuterias','4.3 - Joias_e_bijuterias'),(u'4.4 - Tecidos e armarinho','4.4 - Tecidos e armarinho'),
             (u'5.1 - Transportes','5.1 - Transportes'),(u'6.1 - Produtos_farmaceuticos_e_oticos','6.1 - Produtos_farmaceuticos_e_oticos'),
             (u'6.2 - Servicos_de_saude','6.2 - Servicos_de_saude'),(u'6.3 - Cuidados pessoais','6.3 - Cuidados pessoais'),(u'7.1 - Servicos_pessoais','7.1 - Servicos_pessoais'),
             (u'7.2 - Recreacao_fumo_e_fotografia','7.2 - Recreacao_fumo_e_fotografia'),(u'8.1 - Cursos_leitura_e_papelaria','8.1 - Cursos_leitura_e_papelaria'),
             (u'9.1 - Comunicacao','9.1Comunicacao'))
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
         O peso dos subgrupos eh composto pela soma dos pesos dos itens.
    '''

    nome_subgrupo = models.CharField(max_length=150, choices=SUBGRUPOS)
    peso_subgrupo = models.FloatField(verbose_name="peso do subgrupo")#este campo recebera automaticamente a soma da classe itens.
    data_verificacao_peso = models.DateField()
    grupo_relacionado = models.ForeignKey(pesos_grupos)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_subgrupo

    class Meta:
        verbose_name_plural = "Subgrupos"

class item(models.Model):
    '''
        Os itens serao atualizados periodicamente.
    '''
    nome_item = models.CharField(max_length=150)
    peso = models.FloatField()#valor dado por automatizacao
    data_verificacao = models.DateField()
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_item

    class Meta:
        verbose_name_plural = "Item"

class subitem(models.Model):
    '''
        Cada subitem possui seu pesso, baseando-se na tabela da POF, subitem composto por produto.
    '''

    nome_subitem = models.CharField(max_length=150)
    peso_subitem = models.FloatField(verbose_name="peso do subitem")#valor dados a partir de uma funcao
    item_relacionado = models.ForeignKey(item)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nome_subitem

    class Meta:
        verbose_name_plural = "Subitem"

class produto(models.Model):
    '''
        Os produtos pertencem a um determinado subgrupo, seu preco contarah para a elaboracao do peso desse subgrupo.
    '''

    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=150, blank=True)
    preco = models.FloatField()
    data_verificacao = models.DateField()
    subitem_tipo = models.ForeignKey(subitem)
    ativo = models.BooleanField()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produto"

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
    Local_visitar        = models.ForeignKey(estabelecimento)
    Pesquisador          = models.ForeignKey(perfil)
    data_vizita          = models.DateField()
    grupo__para_pesquisa = models.ForeignKey(pesos_grupos)
    SubGrupoParaPesquisa = models.ForeignKey(subgrupo)
    Item_pesquisado      = models.ForeignKey(item)
    usuario              = models.ForeignKey(User)

    def __unicode__(self):
        return self.Local_visitar

    class Meta:
        verbose_name_plural = "Rota da pesquisa"
