from django.db import models
from django.contrib.auth.models import User
#from geoposition.fields import GeopositionField
#from localflavor.br.models import STATE_CHOICES


# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #endereco = models.CharField(blank=True, null=True, max_length=250, verbose_name='Endereço', help_text='Preencha sem abreviaçoes, exemplo: "Avenida Professor Fonseca Rodrigues, 2001')
    #bairro = models.CharField(blank=True, null=True, max_length=100, help_text='Preencha sem abreviações, ex:"Curitiba')
    #estado = models.CharField(blank=True, null=True, max_length=2, choices=STATE_CHOICES)
    #position = GeopositionField(blank=True, null=True, verbose_name='Geolocalização', help_text='latitude e longitude calculados automaticamente, não altere')

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y  %H:%M')

#a funçao a seguir é para aparecer a data e hora para editar o evento, precisa estar nesse formato
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')