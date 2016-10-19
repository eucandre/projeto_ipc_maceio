from django.db import models
from django.contrib.auth.models import *


GRUPOS = ((u'Aliementacao_e_bebidas','1 - Aliementacao e bebidas'),(u'Habitacao','2 - Habitacao'),(u'Artigos_e_residencia','3 - Artigos e residencia'),
(u'Vestuario','4 - Vestuario'),(u'Transportes','5 - Transportes'),(u'Saude_e_cuidados_especiais','6 - Saude e cuidados especiais'),
(u'Despesas_pessoais','7 - Despesas pessoais'),(u'Educacao','8 - Educacao'),(u'Comunicacao','9 - Comunicao'))

SUBGRUPOS = ((u'AlimentacaoNOdomicilio', '1.1 - Alimentacao no domicilio'),
             (u'AlimentacaoForaDOdomicilio', '1.2 - Alimentacao fora do domicilio'),
             (u'EncargosEmanutencao', '2.1 - Encargos e manutencao'),
             (u'CombustiveisEenergia', '2.2 - Combustiveis e energia'),
             (u'MoveisEutensilios', '3.1 - Moveis e utensilios'),
             (u'AparelhosEletroeletronicos', '3.2 - Aparelhos eletroeletronicos'),
             (u'ConsertosEmanutencao', '3.3 - Consertos e manutencao'), (u'4.1 - Roupas', '4.1 - Roupas'),
             (u'CalcadosEacessorios', '4.2 - Calcados e assessorios'),
             (u'JoiasEbijuterias', '4.3 - Joias e bijuterias'),
             (u'TecidosEarmarinho', '4.4 - Tecidos e armarinho'),
             (u'Transportes', '5.1 - Transportes'),
             (u'ProdutosFarmaceuticosEoticos', '6.1 - Produtos farmaceuticos e oticos'),
             (u'ServicosDEsaude', '6.2 - Servicos de saude'),
             (u'CuidadosPessoais', '6.3 - Cuidados pessoais'),
             (u'ServicosPessoais', '7.1 - Servicos pessoais'),
             (u'RecreacaoFumoEfotografia', '7.2 - Recreacao fumo e fotografia'),
             (u'CursosLeituraEpapelaria', '8.1 - Cursos leitura e papelaria'),
             (u'Comunicacao', '9.1 - Comunicacao'))

VINCULO = ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'), (u'Estagiario','Estagiario'))
ATIVO = ((u'Ativo','Ativo'), (u'Inativo','Inativo'))

class Establishment(models.Model):
    '''
        Esta estrutura conta com o endereco fisico e o contato do estabelecimento, marca se o mesmo ainda esta ativo.
    '''
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150)
    active = models.CharField(choices=ATIVO, max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Estabelecimentos com enderecos e contatos'

class Group(models.Model):
    name = models.CharField(choices=GRUPOS, max_length=150)
    weight = models.FloatField()
    date = models.DateField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Grupo de itens de produtos e de servicos para o consumidor'

class SubGroup(models.Model):

    name = models.CharField(choices=SUBGRUPOS, max_length=150)
    weight = models.FloatField()
    group = models.ForeignKey(Group)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subgrupos de itens para produtos e servicos'

class Item(models.Model):
    '''
        Cada item pertence a um subgrupo, os itens possuem pesos determinados a partir do valor dos precos dos subitem.
        O valor do weight(peso) de cada item eh dado automaticamente. Este modulo eh para administracao do sistema ipc.
        Atualizado todo inicio de mes o peso de cada item.
    '''
    name = models.CharField(max_length=150)
    weight = models.FloatField()
    sub_group = models.ForeignKey(SubGroup)
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

class Profile(models.Model):
    '''
        Cadastro de participadores do ipc.
        Possui ligacao, desde quando estah ativo e se esta ativo.
    '''
    name = models.CharField(max_length=150)
    bond = models.CharField(max_length=150, choices=VINCULO)
    since = models.DateField()
    active = models.CharField(choices=ATIVO, max_length=150)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Perfil de usuarios do sistema do ipc maceio'

class Rout(models.Model):
    '''A pesquisa eh realizada por um pesquisador.
    O construtor retornara o tamanho do products.
    '''
    profile_searcher = models.ForeignKey(Profile)
    establishment = models.ForeignKey(Establishment)
    products = models.ManyToManyField(Product)

    def __unicode__(self):
        return self.profile_searcher.__str__()

    class Meta:
        verbose_name_plural = 'Rota para a catalogacao dos precos de um conjunto de produtos'

class Search(models.Model):
    rout = models.ForeignKey(Rout)
    value_product = models.FloatField()

    def __unicode__(self):
        return self.rout.__str__()



