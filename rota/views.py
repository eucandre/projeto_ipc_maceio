from django.contrib.auth import authenticate, login, logout
from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from rota.forms import *


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
    return render_to_response("paginas_da_rota/criar_rota.html",{"form":form, "usuario":usu})
