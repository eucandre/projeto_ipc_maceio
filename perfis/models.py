from django.db import models

class perfil(models.Model):
    Nome_pesquisador = models.CharField(max_length=150)

    def __unicode__(self):
        return self.Nome_pesquisador
