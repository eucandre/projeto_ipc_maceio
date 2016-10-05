__author__ = 'Carlos'

from django import forms
from models import *
from datetime import *

GRUPOS = ((u'Aliementacao_e_bebidas','1 - Aliementacao e bebidas'),(u'Habitacao','2 - Habitacao'),(u'Artigos_e_residencia','3 - Artigos e residencia'),
            (u'Vestuario','4 - Vestuario'),(u'Transportes','5 - Transportes'),(u'Saude_e_cuidados_especiais','6 - Saude e cuidados_especiais'),
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

class FormItem(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Item'}))
    weight = forms.CharField(max_length=150, label='Peso',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso do item'}))
    sub_group = forms.ModelChoiceField(queryset=SubGroup.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Grupo relacionado'}))
    date = forms.DateField(label='Data do registro', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de entrada de dados'}))
    class Meta:
        model = Item
        fields = ['name','weight','sub_group','date']

class FormSubitem(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Nome',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Sub-item'}))
    weight = forms.CharField(max_length=150, label='Peso',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso do subitem'}))
    item = forms.ModelChoiceField(queryset=Item.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Item relacionado'}))
    date = forms.DateField(label='Data do registro', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de entrada de dados'}))

    class Meta:
        model = Subitem
        fields = ['name','weight','item', 'date']

class FormProduto(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}))
    mark = forms.CharField(max_length=150, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca do produto'}))
    amount_per_price = forms.CharField(max_length=150, label='Preco por unidade',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preco por unidade'}))
    item = forms.ModelChoiceField(queryset=Item.objects.all(), label='item', widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Item relacionado'}))
    active = forms.ChoiceField(choices=ATIVO, label='Situacao', widget=forms.RadioSelect(attrs={'class': 'checkbox-inline'}))
    class Meta:
        model = Product
        fields = ['name', 'mark', 'amount_per_price', 'item', 'active']