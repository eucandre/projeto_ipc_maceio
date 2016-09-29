from django.db.backends.mysql.base import django_conversions
from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from app_projeto_ipc.forms import *
from calculo_para_laspeyre import *

#criar os usuarios e seus loggins, o acesso sera somente com acesso dos usuarios (Feito)
#criar a edicao do perfil do usuario, podendo mudar a senha e o nome que de usuario.
#cada usuario cadastrado podera editar suas atividades, mesmo depois de salvas.
#criar um banco para os arquivos excluidos, servir de um backup de serguranca, para quando errarem a exclusao ser possivel recuperar.


def acesso(request):

    return render_to_response("paginas_do_sistema/login.html")

def apresentacao(request):
    return render_to_response("paginas_do_sistema/pagina_apresentacao.html",{})


def sub_grupos(request):
    if request.method == 'POST':
        form = FormSubgrupo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FormSubgrupo()
    return render_to_response("paginas_do_sistema/subgrupos.html",{"form":form}, context_instance = RequestContext(request))


def pesos_grupos(request):
    '''
    Esta funcao ira guardar os pesos baseando-se na tabela pof. quem modifica esta funcao eh apenas o adm. geral.
    '''
    if request.method == 'POST':
        form = FormPesos_grupos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FormPesos_grupos()
    return render_to_response("paginas_do_sistema/pesos_grupos.html",{"form":form}, context_instance = RequestContext(request))

def criacao_rota(request):
    if request.method =='POST':
        form = FORMrota(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FORMrota()
    return render_to_response("paginas_da_rota/criar_rota.html",{"form":form} , context_instance = RequestContext(request))


def perfil(request):
    if request.method == 'POST':
        form  = Formperfil(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Formperfil()
    return render_to_response("paginas_perfil/index.html",{"form":form}, context_instance = RequestContext(request))

def estabelecimento(request):
    if request.method=='POST':
        form = FORMestabelecimento(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FORMestabelecimento()
    return render_to_response("paginas_estabelecimento/index.html",{"form":form}, context_instance = RequestContext(request))

def item(request):
    if request.method == 'POST':
        form = FormItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FormItem()
    return render_to_response("paginas_item/index.html" ,{"form":form}, context_instance = RequestContext(request))

def subitem(request):
    if request.method == 'POST':
        form  = FormSubitem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FormSubitem()
    return render_to_response("paginas_subitem/index.html",{"form":form}, context_instance = RequestContext(request) )
    
def produto(request):
    if request.method =='POST':
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FormProduto()
    return render_to_response("paginas_produtos/index.html", {"form":form}, context_instance = RequestContext(request))

def ColetaPrecos(request):
    if request.method =='POST':
        form = FormColetaPrecos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FormColetaPrecos()
    return render_to_response("coleta_precos/index.html",{"form":form}, context_instance = RequestContext(request))
