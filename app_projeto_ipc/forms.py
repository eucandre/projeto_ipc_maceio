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

VINCULO =  ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'), (u'Estagiario','Estagiario'))
ATIVO = ((u'Ativo','Ativo'), (u'Inativo','Inativo'))

class FormEstablishment(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Nome',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do estabelecimento'}))
    street = forms.CharField(max_length=150, label='Rua' , widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rua do estabelecimento'}))
    neighborhood = forms.CharField(max_length=150, label='Bairro',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Bairro do estabelecimento'}))
    email = forms.CharField(max_length=150, label='E-mail',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail do estabelecimento'}))
    phone = forms.CharField(max_length=150, label='Telefone',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefone do estabelecimento'}))
    active = forms.ChoiceField(choices=ATIVO, label='Situacao',widget=forms.RadioSelect(attrs={'class':'checkbox-inline'}))
    class Meta:
        model = Establishment
        fields = ['name', 'street', 'neighborhood', 'email','phone', 'active']

class FormProfile(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do perfil'}))
    since = forms.DateField(label='Liagado desde',widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Data de entrada no ipc'}))
    bond = forms.ChoiceField(choices=VINCULO,label='Vinculo',widget=forms.RadioSelect(attrs={'class':'checkbox-inline'}))
    active = forms.ChoiceField(choices=ATIVO, label='Situacao',widget=forms.RadioSelect(attrs={'class':'checkbox-inline'}))

    class Meta:
        model = Profile
        fields = ['name', 'since', 'bond', 'active']

class FormGroup(forms.ModelForm):
    name = forms.ChoiceField(choices=GRUPOS, label='Nome',widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nome do grupo'}))
    weight = forms.CharField(max_length=150, label='Peso',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso do grupo'}))
    date = forms.DateField(label='Data do registro',widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de entrada de dados'}))
    class Meta:
        model = Group
        fields = ['name', 'weight', 'date']

class FormSubgrupo(forms.ModelForm):
    name = forms.ChoiceField(choices=SUBGRUPOS, label='Nome',widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nome do Sub-grupo'}))
    weight = forms.CharField(max_length=150, label='Peso',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso do grupo'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Grupo relacionado'}))
    date = forms.DateField(label='Data do registro', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de entrada de dados'}))
    class Meta:
        model = SubGroup
        fields = ['name', 'weight', 'group','date']

class FormSubitem(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Sub-item'}))
    weight = forms.CharField(max_length=150, label='Peso',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso do item'}))
    item = forms.ModelChoiceField(queryset=Item.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Item relacionado'}))
    date = forms.DateField(label='Data do registro', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de entrada de dados'}))
    class Meta:
        model = Subitem
        fields = ['name','weight','item', 'date']