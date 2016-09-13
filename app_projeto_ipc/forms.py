__author__ = 'Carlos'

from django import forms
from models import *

GRUPOS = ((u'Aliemntacao_e_bebidas','Aliemntacao_e_bebidas'),(u'Habitacao','Habitacao'),(u'Artigos_e_residencia','Artigos_e_residencia'),
(u'Vestuario','Vestuario'),(u'Transportes','Transportes'),(u'Saude_e_cuidados_especiais','Saude_e_cuidados_especiais'),
(u'Despesas_pessoais','Despesas_pessoais'),(u'Educacao','Educacao'),(u'Comunicacao','Comunicao'))

VINCULO =  ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'))

class FormPesos_grupos(forms.ModelForm):
    grupo = forms.ChoiceField(choices=GRUPOS, widget=forms.Select(attrs={"class":"form-control"}))
    peso = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control","mask": "99-999999"}))

    class Meta:
        model = pesos_grupos
        fields = ['grupo','peso','usuario']

class FormSubgrupo(forms.ModelForm):
    nome_subgrupo = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))
    peso_subgrupo = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control"}))
    grupo_relacionado = forms.ModelChoiceField(queryset=pesos_grupos.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    class Meta:
        model = subgrupo
        fields = ['usuario',]

class FormItem(forms.ModelForm):
    class Meta:
        model = item
        fields = ['nome_item','usuario']

class FormSubitem(forms.ModelForm):
    class Meta:
        model = subitem
        firlds = ['nome_subitem','peso_subitem','item_relacionado','usuario']

class FORMestabelecimento(forms.ModelForm):
    NomeDoEstabeleciemento = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "label":"Nome"}))
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