from django.db import models

# Create your models here.
class primary(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)
    con_password=models.CharField(max_length=10)
    address=models.TextField(max_length=300,default='NA')

    def __str__(self):
        return str(self.id) + '-' + self.name

