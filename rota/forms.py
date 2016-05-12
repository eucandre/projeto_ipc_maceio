from rotas_app.models import *
from django import forms

class FORMestabelecimento(forms.ModelForm):
    
    class Meta:
        model = estabelecimento
        fields = ['NomeDoEstabeleciemento','Bairro','Rua','TeleFone','Email','usuario']

class FORMrota(forms.ModelForm):
    class Meta:
        model = rota
        fields =['Local_vizitar','Pesquisador','data_vizita','grupo__para_pesquisa','SubGrupoParaPesquisa','Item_pesquisado','usuario']









