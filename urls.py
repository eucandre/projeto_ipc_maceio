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
    url(r'^sub_grupos/$','app_projeto_ipc.views.registra_grupos'),
    url(r'^peso_grupos/$','app_projeto_ipc.views.pesos_grupos'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #-----------Rota------------------
    url(r'^cria_rota/$','app_projeto_ipc.views.criacao_rota'),
    url(r'^perfil/$','app_projeto_ipc.views.perfil'),
    url(r'^estabelecimento','app_projeto_ipc.views.estabelecimento'),
    #

    (r'^login/$',"django.contrib.auth.views.login",{"template_name":"paginas_do_sistema/login.html"}),
    (r'^logout/$',"django.contrib.auth.views.logout_then_login",{"login_url":"/login/"}),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
