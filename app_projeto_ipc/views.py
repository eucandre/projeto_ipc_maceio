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
    usuario = None
    if request.user.is_authenticated():
        usuario = request.user.username
    return render_to_response("paginas_do_sistema/pagina_apresentacao.html",{"usuario":usuario})


def sub_grupos(request):
    if request.method == "post":
        form = FormSubgrupo(request.FILES, request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
    else:
        form = FormSubgrupo()
    return render_to_response("paginas_do_sistema/subgrupos.html",{"form":form}, context_instance = RequestContext(request))


def pesos_grupos(request):
    '''
    Esta funcao ira guardar os pesos baseando-se na tabela pof. quem modifica esta funcao eh apenas o adm. geral.
    '''

    usu = None
    if request.user.is_authenticated():
        usu = request.user.username
    if request.method == 'POST':
        form = FormPesos_grupos(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FormPesos_grupos()
    return render_to_response("paginas_do_sistema/pesos_grupos.html",{"form":form,"usuario":usu}, context_instance = RequestContext(request))

def criacao_rota(request):
    usu = None
    if request.user.is_authenticated():
        usu = request.user.username
    if request.method =="post":
        form = FORMrota(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
            return render_to_response("arquivo_auxiliar/salvo.html",{})
    else:
        form = FORMrota()
    return render_to_response("paginas_da_rota/criar_rota.html",{"form":form, "usuario":usu} , context_instance = RequestContext(request))


def perfil(request):
    usu = None
    if request.user.is_authenticated():
        usu = request.user.username
    if request.method == "POST":
        form  = Formperfil(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
    else:
        form = Formperfil()
    return render_to_response("paginas_perfil/index.html",{"form":form, "usuario":usu}, context_instance = RequestContext(request))

def estabelecimento(request):
    if request.method=="post":
        form = FORMestabelecimento(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
    else:
        form = FORMestabelecimento()
    return render_to_response("paginas_estabelecimento/index.html",{"form":form}, context_instance = RequestContext(request))

def produto(request):
    if request.method =="post":
        form = FormProduto(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()
    else:
        form = FormProduto()
    return render_to_response("paginas_produtos/index.html", {"form":form}, context_instance = RequestContext(request))

def calcula_laspeyres(request):
    usu = None
    if request.method == "post":
        pass