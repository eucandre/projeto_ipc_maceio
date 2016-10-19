from django.db.backends.mysql.base import django_conversions
from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from app_projeto_ipc.forms import *
from calculo_para_laspeyre import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

#criar os usuarios e seus loggins, o acesso sera somente com acesso dos usuarios (Feito)
#criar a edicao do perfil do usuario, podendo mudar a senha e o nome que de usuario.
#cada usuario cadastrado podera editar suas atividades, mesmo depois de salvas.
#criar um banco para os arquivos excluidos, servir de um backup de serguranca, para quando errarem a exclusao ser possivel recuperar.


def acesso(request):

    return render_to_response('paginas_do_sistema/login.html')

def apresentacao(request):
    return render_to_response('paginas_do_sistema/pagina_apresentacao.html')

def EstabelecimentoCadastro(request):
    if request.method == 'POST':
        form = FormEstablishment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormEstablishment()
    return render_to_response('paginas_estabelecimento/index.html', {'form':form}, RequestContext(request))

def PerfilCadastro(request):
    if request.method == 'POST':
        form = FormProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormProfile()
    return render_to_response('paginas_perfil/index.html', {'form':form}, RequestContext(request))

def GrupoCadastro(request):
    if request.method == 'POST':
        form = FormGroup(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormGroup()
    return render_to_response('paginas_do_sistema/grupos.html', {'form':form}, RequestContext(request))

def SubgrupoCadastro(request):
    if request.method == 'POST':
        form = FormSubgrupo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormSubgrupo()
    return render_to_response('paginas_do_sistema/subgrupos.html', {'form':form}, RequestContext(request))

def ItemCadastro(request):
    if request.method == 'POST':
        form = FormItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormItem()
    return render_to_response('paginas_item/index.html', {'form':form}, RequestContext(request))

def SubitemCadastro(request):
    if request.method == 'POST':
        form = FormSubitem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormSubitem()
    return render_to_response('paginas_subitem/index.html', {'form':form}, RequestContext(request))

def ProdutoCadastro(request):
    if request.method == 'POST':
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormProduto()
    return render_to_response('paginas_produtos/index.html', {'form':form}, RequestContext(request))

def RoutCadastro(request):
    if request.method == 'POST':
        form = FormRout(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormRout()
    return render_to_response('paginas_da_rota/index.html', {'form':form}, RequestContext(request))

def SearchCadastro(request):
    if request.method == 'POST':
        form = FormSearch(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('arquivo_auxiliar/salvo.html', {})
    else:
        form = FormSearch()
    return render_to_response('paginas_search/index.html', {'form':form}, RequestContext(request))