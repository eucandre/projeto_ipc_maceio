from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ipc.views.home', name='home'),
    # url(r'^ipc/', include('ipc.foo.urls')),
    #url(r'^$','app_ipc.views.acesso'),
    url(r'^$','app_projeto_ipc.views.apresentacao'),
    url(r'^estabelecimento', 'app_projeto_ipc.views.EstabelecimentoCadastro'),
    url(r'^perfil', 'app_projeto_ipc.views.PerfilCadastro'),
    url(r'^grupo', 'app_projeto_ipc.views.GrupoCadastro'),
    url(r'^subgrupo', 'app_projeto_ipc.views.SubgrupoCadastro'),
    url(r'^subitem', 'app_projeto_ipc.views.SubitemCadastro'),
    url(r'^item', 'app_projeto_ipc.views.ItemCadastro'),
    url(r'^produto', 'app_projeto_ipc.views.ProdutoCadastro'),
    url(r'^rota', 'app_projeto_ipc.views.RotaCadastro'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #-----------Rota------------------
    #

    (r'^login/$',"django.contrib.auth.views.login",{"template_name":"paginas_do_sistema/login.html"}),
    (r'^logout/$',"django.contrib.auth.views.logout_then_login",{"login_url":"/login/"}),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
