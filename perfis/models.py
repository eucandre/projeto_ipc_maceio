from django.db import models
from django.contrib.auth.models import *

VINCULO =  ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'))

class perfil(models.Model):
    '''
        Esta classe tem a funcionalidade de cadastrar o perfil dos participantes do ipc para controlar as pesquisas realizadas.
    '''
    nome_pesquisador = models.CharField(max_length=150)
    vinculo = models.CharField(choices=VINCULO, max_length=150)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.Nome_pesquisador
