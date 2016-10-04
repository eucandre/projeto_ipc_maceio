from django.db import models
from django.contrib.auth.models import *
from sphinx.builders.gettext import I18nBuilder

GRUPOS = ((u'Aliementacao_e_bebidas','1 - Aliementacao e bebidas'),(u'Habitacao','2 - Habitacao'),(u'Artigos_e_residencia','3 - Artigos e residencia'),
(u'Vestuario','4 - Vestuario'),(u'Transportes','5 - Transportes'),(u'Saude_e_cuidados_especiais','6 - Saude e cuidados especiais'),
(u'Despesas_pessoais','7 - Despesas pessoais'),(u'Educacao','8 - Educacao'),(u'Comunicacao','9 - Comunicao'))

SUBGRUPOS = ((u'Alimentacao_no_domicilio', '1.1 - Alimentacao no domicilio'),
             (u'Alimentacao_fora_do_domicilio', '1.2 - Alimentacao fora do domicilio'),
             (u'Encargos_e_manutencao', '2.1 - Encargos e manutencao'),
             (u'Combustiveis_e_energia', '2.2 - Combustiveis e energia'),
             (u'Moveis_e_utensilios', '3.1 - Moveis e utensilios'),
             (u'Aparelhos_eletroeletronicos', '3.2 - Aparelhos eletroeletronicos'),
             (u'Consertos_e_manutencao', '3.3 - Consertos e manutencao'), (u'4.1 - Roupas', '4.1 - Roupas'),
             (u'Calcados_e_acessorios', '4.2 - Calcados e assessorios'),
             (u'Joias_e_bijuterias', '4.3 - Joias e bijuterias'),
             (u'Tecidos e armarinho', '4.4 - Tecidos e armarinho'),
             (u'Transportes', '5.1 - Transportes'),
             (u'Produtos_farmaceuticos_e_oticos', '6.1 - Produtos farmaceuticos e oticos'),
             (u'Servicos_de_saude', '6.2 - Servicos de saude'),
             (u'Cuidados pessoais', '6.3 - Cuidados pessoais'),
             (u'Servicos_pessoais', '7.1 - Servicos pessoais'),
             (u'Recreacao_fumo_e_fotografia', '7.2 - Recreacao fumo e fotografia'),
             (u'Cursos_leitura_e_papelaria', '8.1 - Cursos leitura e papelaria'),
             (u'Comunicacao', '9.1 - Comunicacao'))

VINCULO =    ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'), (u'Bolsista','Bolsista'))
ATIVO = ((u'Ativo','Ativo'), (u'Inativo','Inativo'))

class Establishment(models.Model):
    '''

    '''
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telphone = models.CharField(max_length=150)
    active = models.CharField(choices=ATIVO, max_length=150)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Estabelecimentos com enderecos e contatos'
class Item(models.Model):
    '''
        Cada item pertence a um subgrupo, os itens possuem pesos determinados a partir do valor dos precos dos subitem.
        O valor do weight(peso) de cada item eh dado automaticamente. Este modulo eh para administracao do sistema ipc.
        Atualizado todo inicio de mes o peso de cada item.
    '''
    name = models.CharField(max_length=150)
    weight = models.FloatField()
    sub_group = models.CharField(max_length=150, choices=SUBGRUPOS)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Item, servicos ou produtos ao consumidor'
        db_table = 'item'

class Subitem(models.Model):
    '''
        Os subitem constituem os Item, sao constituidos dos pesos dos products, weight(peso) eh dado automaticamente.
    '''
    name = models.CharField(max_length=150)
    weight = models.FloatField()
    item = models.ForeignKey(Item)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub-itens para produtos e servicos'

class Product(models.Model):
    '''
        Cadastramento e busca de produtos e servicos disponiveis no mercado.
        Cada produto pertence a um tipo de item, exemplo de itens: Cereais, mecanica, etc.
        O preco eh dado pela quantidade de produtos(amount_per_price).
    '''
    name = models.CharField(max_length=150)
    mark = models.CharField(max_length=150)
    amount_per_price = models.CharField(max_length=150)
    item = models.ForeignKey(Item)
    active = models.CharField(choices=ATIVO, max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Produtos e servicos para o consumidor'
        db_table = 'produto'


