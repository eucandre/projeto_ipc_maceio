__author__ = 'Carlos'

from django import forms
from models import *

GRUPOS = ((u'Aliemntacao_e_bebidas','Aliemntacao_e_bebidas'),(u'Habitacao','Habitacao'),(u'Artigos_e_residencia','Artigos_e_residencia'),
(u'Vestuario','Vestuario'),(u'Transportes','Transportes'),(u'Saude_e_cuidados_especiais','Saude_e_cuidados_especiais'),
(u'Despesas_pessoais','Despesas_pessoais'),(u'Educacao','Educacao'),(u'Comunicacao','Comunicao'))

SUBGRUPOS = ((u'Alimentacao_no_domicilio', '1.1 - Alimentacao no domicilio'),
             (u'Alimentacao_fora_do_domicilio', '1.2 - Alimentacao fora do domicilio'),
             (u'Encargos_e_manutencao', '2.1 - Encargos e manutencao'),
             (u'Combustiveis_e_energia', '2.2 - Combustiveis e energia'),
             (u'Moveis_e_utensilios', '3.1 - Moveis e utensilios'),
             (u'Aparelhos_eletroeletronicos', '3.2 - Aparelhos eletroeletronicos'),
             (u'Consertos_e_manutencao', '3.3 - Consertos e manutencao'), (u'4.1 - Roupas', '4.1 - Roupas'),
             (u'Calcados_e_acessorios', '4.2 Calcados e assessorios'),
             (u'Joias_e_bijuterias', '4.3 - Joias e bijuterias'),
             (u'Tecidos e armarinho', '4.4 - Tecidos e armarinho'),
             (u'Transportes', '5.1 - Transportes'),
             (u'Produtos_farmaceuticos_e_oticos', '6.1 - Produtos farmaceuticos e oticos'),
             (u'Servicos_de_saude', '6.2 - Servicos de saude'),
             (u'Cuidados pessoais', '6.3 - Cuidados pessoais'),
             (u'Servicos_pessoais', '7.1 - Servicos pessoais'),
             (u'Recreacao_fumo_e_fotografia', '7.2 - Recreacao_fumo e fotografia'),
             (u'Cursos_leitura_e_papelaria', '8.1 - Cursos_leitura e papelaria'),
             (u'Comunicacao', '9.1 - Comunicacao'))

VINCULO =  ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'))

class FormPesos_grupos(forms.ModelForm):
    grupo = forms.ChoiceField(choices=GRUPOS, widget=forms.Select(attrs={"class":"form-control"}))
    peso = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control","mask": "99-999999"}))

    class Meta:
        model = pesos_grupos
        fields = ['grupo','peso','usuario']

class FormSubgrupo(forms.ModelForm):
    nome_subgrupo = forms.ChoiceField(choices=SUBGRUPOS , widget=forms.Select(attrs={"class":"form-control"}))
    peso_subgrupo = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    grupo_relacionado = forms.ModelChoiceField(queryset=pesos_grupos.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    class Meta:
        model = subgrupo
        fields = ['usuario']

class FormItem(forms.ModelForm):
    class Meta:
        model = item
        fields = ['nome_item','usuario']

class FormSubitem(forms.ModelForm):
    class Meta:
        model = subitem
        fields = ['nome_subitem','peso_subitem','item_relacionado','usuario']

class FormProduto(forms.ModelForm):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    marca = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    preco = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    data_verificacao = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}))
    sub_item = forms.ModelChoiceField(queryset=subitem.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    ativo = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"form-control"}))
    class Meta:
        model = produto
        fields = ['usuario']

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
        fields =['usuario']


class Formperfil(forms.ModelForm):
    nome_pesquisador = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Nome"}))
    vinculo = forms.ChoiceField(choices=VINCULO, widget=forms.Select(attrs={"class":"form-control", "placeholder":"Vinculo"}))
    class Meta:
        model = perfil
        fields = ['usuario']