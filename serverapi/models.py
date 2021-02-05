from django.db import models

class server(models.Model):
    Server_ram = models.CharField(max_length=55)
    Server_cpu = models.CharField(max_length=55)
    Server_os = models.CharField(max_length=55)
    Server_graphic = models.CharField(max_length=100)
    Server_storage = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)