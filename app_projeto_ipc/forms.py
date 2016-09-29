__author__ = 'Carlos'

from django import forms
from models import *
from datetime import *

GRUPOS = ((u'Aliementacao_e_bebidas','1 - Aliementacao e bebidas'),(u'Habitacao','2 - Habitacao'),(u'Artigos_e_residencia','3 - Artigos e residencia'),
            (u'Vestuario','4 - Vestuario'),(u'Transportes','5 - Transportes'),(u'Saude_e_cuidados_especiais','6 - Saude e cuidados_especiais'),
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

VINCULO =  ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'))

class FormPesos_grupos(forms.ModelForm):
    grupo = forms.ChoiceField(choices=GRUPOS, widget=forms.Select(attrs={"class":"form-control"}))
    peso = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control","mask": "99-999999"}))

    class Meta:
        model = pesos_grupos

class FormSubgrupo(forms.ModelForm):
    nome_subgrupo = forms.ChoiceField(choices=SUBGRUPOS , widget=forms.Select(attrs={"class":"form-control"}))
    peso_subgrupo = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    grupo_relacionado = forms.ModelChoiceField(queryset=pesos_grupos.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    data_verificacao_peso = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"DD/MM/AAAA"}))
    class Meta:
        model = subgrupo

class FormItem(forms.ModelForm):
    nome_item = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    sub_grupo  = forms.ModelChoiceField(queryset=subgrupo.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    peso = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    data_verificacao = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"DD/MM/AAAA"}))
    class Meta:
        model = item

class FormSubitem(forms.ModelForm):
    nome_subitem = forms.CharField(max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
    peso_subitem = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))#valor dados a partir de uma funcao
    item_relacionado = forms.ModelChoiceField(queryset=item.objects.all(), widget= forms.Select(attrs={"class":"form-control"}))

    class Meta:
        model = subitem

class FormProduto(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    marca = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    preco = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    data_verificacao = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"DD/MM/AAAA"}))
    sub_item = forms.ModelChoiceField(queryset=subitem.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    ativo = forms.BooleanField(required=False, initial=False ,widget=forms.CheckboxInput(attrs={"class":"checkbox"}), help_text="Se o produto esta ativo")
    class Meta:
        model = produto

class FORMestabelecimento(forms.ModelForm):
    Nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "label":"Nome"}))
    Bairro = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    Rua = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    TeleFone = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    Email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = estabelecimento

class FORMrota(forms.ModelForm):
    local_visitar = forms.ModelChoiceField(queryset=estabelecimento.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    pesquisador = forms.ModelChoiceField(queryset=perfil.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    data_visita = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "placeholder":"DD/MM/AAAA"}))
    grupo__para_pesquisa = forms.ModelChoiceField(queryset=pesos_grupos.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    sub_grupo = forms.ModelChoiceField(queryset=subgrupo.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    item_pesquisa = forms.ModelChoiceField(queryset=item.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    class Meta:
        model = rota


class Formperfil(forms.ModelForm):
    nome_pesquisador = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Nome"}))
    vinculo = forms.ChoiceField(choices=VINCULO, widget=forms.Select(attrs={"class":"form-control", "placeholder":"Vinculo"}))
    class Meta:
        model = perfil


class FormColetaPrecos(forms.ModelForm):
    
    estabelecimento = forms.ModelChoiceField(queryset=rota.objects.all(),widget=forms.Select(attrs={"class":"form-control", "placeholder":"Estabelecimento"}))
    pesquisador = forms.CharField(widget=forms.Select(attrs={"class":"form-control", "placeholder":"Pesquisador"}))
    #grupo_pesquisa = forms.ModelChoiceField(queryset=pesos_grupos.objects.all(),widget=forms.Select(attrs={"class":"form-control", "placeholder":"Grupo"}))
    #sub_grupo = forms.ModelChoiceField(queryset=subgrupo.objects.all(),widget=forms.Select(attrs={"class":"form-control", "placeholder":"Subgrupo"}))
    #item = forms.ModelChoiceField(queryset=item.objects.all(),widget=forms.Select(attrs={"class":"form-control", "placeholder":"Item"}))
    #subitem = forms.ModelMultipleChoiceField(queryset=subitem.objects.all(),widget=forms.Select(attrs={"class":"form-control", "placeholder":"Subitem"}))
    produto_de_pesquisa = forms.ModelMultipleChoiceField(queryset=produto.objects.all(),widget=forms.CheckboxSelectMultiple())
    preco_unidade_produto = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Preco produto"}))
    #unidade = forms.IntegerField(help_text="UN, Kg, etc.",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Quantidade"}))
    somatorio_precos = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Somatorio"}))
    
    class Meta:
        model = ColetaPrecos
