from django.db import models

VINCULO =   ((u'Bolsista','Bolsista'),(u'Comissionado','Comissionado'), (u'Efetivo', 'Efetivo'))

class perfil(models.Model):
    Nome_pesquisador = models.CharField(max_length=150)
    vinculo = models.CharField(choices=VINCULO, max_length=150)
    def __unicode__(self):
        return self.Nome_pesquisador
