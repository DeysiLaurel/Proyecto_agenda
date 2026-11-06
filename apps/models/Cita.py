from django.db import models
from .Cliente import Cliente

class Cita(models.Model):
   
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='client_id')
    
    asunto = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    direccion = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    
   
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'citas'  
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'

    def __str__(self):
        return f"Cita {self.id} - {self.asunto} ({self.fecha} {self.hora})"