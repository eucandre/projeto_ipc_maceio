from django.db import models
from django.contrib.auth.models import *

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
             (u'Recreacao_fumo_e_fotografia', '7.2 - Recreacao_fumo e fotografia'),
             (u'Cursos_leitura_e_papelaria', '8.1 - Cursos leitura e papelaria'),
             (u'Comunicacao', '9.1 - Comunicacao'))

VINCULO =    ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'), (u'Bolsista','Bolsista'))

class pesos_grupos(models.Model):
    '''
        A finalidade desta classe eh possibilitar a atribuicao dos pesos dos grupos, quando necessario a mudanca, sem a necessidade
    de mexer em linha de codigo e permitir que o administrador do projeto edite sem prejuizo ao sistema.
    '''
    grupo = models.CharField(choices=GRUPOS, max_length=150)
    peso = models.FloatField()
    
    def __unicode__(self):
        return self.grupo

    class Meta:
        verbose_name_plural = "Pesos grupos"
        db_table = 'grupo'

class subgrupo(models.Model):
    '''
         O peso dos subgrupos eh composto pela soma dos pesos dos itens.
    '''
    nome_subgrupo = models.CharField(max_length=150, choices=SUBGRUPOS)
    peso_subgrupo = models.FloatField()#este campo recebera automaticamente a soma da classe itens.
    data_verificacao_peso = models.DateField()
    grupo_relacionado = models.ForeignKey(pesos_grupos)
    

    def __unicode__(self):
        return self.nome_subgrupo

    class Meta:
        verbose_name_plural = "Subgrupos"
        db_table = 'subgrupo'

class item(models.Model):
    '''
        Sao compostos por subitens
    '''
    nome_item = models.CharField(max_length=150)
    sub_grupo = models.ForeignKey(subgrupo)
    peso = models.FloatField()#valor dado por automatizacao
    data_verificacao = models.DateField()
    

    def __unicode__(self):
        return self.nome_item

    class Meta:
        verbose_name_plural = "Item"
        db_table = 'item'

class subitem(models.Model):
    '''
        Cada subitem possui seu pesso, baseando-se na tabela da POF, subitem composto por produto.
    '''
    nome_subitem = models.CharField(max_length=150)
    peso_subitem = models.FloatField(verbose_name="peso do subitem")#valor dados a partir de uma funcao
    item_relacionado = models.ForeignKey(item)
    

    def __unicode__(self):
        return self.nome_subitem

    class Meta:
        verbose_name_plural = "Subitem"
        db_table = 'subitem'

class produto(models.Model):
    '''
        Os produtos pertencem a um determinado subgrupo, seu preco contarah para a elaboracao do peso desse subgrupo.
    '''
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=150, blank=True)
    data_verificacao = models.DateField()
    subitem_tipo = models.ForeignKey(subitem)
    ativo = models.BooleanField(default=False)
    

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produto"
        db_table = 'produto'

class perfil(models.Model):
    '''
        Esta classe tem a funcionalidade de cadastrar o perfil dos participantes do ipc para controlar as pesquisas realizadas.
    '''
    nome_pesquisador = models.CharField(max_length=150)
    vinculo = models.CharField(choices=VINCULO, max_length=150)
    

    def __unicode__(self):
        return self.nome_pesquisador

    class Meta:
        verbose_name_plural = "Perfil"
        db_table = 'perfil'

class estabelecimento(models.Model):
    '''
        Classe para o cadastramento da localizacao do estabelecimento
    '''
    Nome     = models.CharField(max_length=150)
    Bairro   = models.CharField(max_length=150)
    Rua      = models.CharField(max_length=150)
    TeleFone = models.CharField(max_length=150, blank=True)
    Email    = models.EmailField(blank=True)
    

    def __unicode__(self):
        return self.Nome

    class Meta:
        verbose_name_plural = "Estabelecimento"
        db_table = "estabalecimento"

class rota(models.Model):
    '''
        Seleciona a rota a ser seguida, esta classe tera uma funcionalidade automatizada.
    '''
    Local_visitar        = models.ForeignKey(estabelecimento)
    Pesquisador          = models.ForeignKey(perfil)
    data_vizita          = models.DateField()
    grupo__para_pesquisa = models.ManyToManyField(pesos_grupos)
    SubGrupoParaPesquisa = models.ManyToManyField(subgrupo)
    Item_pesquisado      = models.ManyToManyField(item)
    subitem              = models.ManyToManyField(subitem)
    

    def __unicode__(self):
        return self.Local_visitar

    class Meta:
        verbose_name_plural = "Rota da pesquisa"

class ColetaPrecos(models.Model):
    """
        Responsavel pela coleta de precos dos produtos da pesquisa
    """
    local               = models.ForeignKey(rota)
    produto_de_pesquisa = models.ManyToManyField(produto)
    precos              = models.FloatField()
    somatorio_precos    = models.FloatField()
    

    def __unicode__(self):
        return self.local

    class Meta:
        verbose_name_plural = "Coleta de precos"
        db_table = 'coleta'