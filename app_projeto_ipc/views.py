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

    return render_to_response('paginas_do_sistema/login.html')

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