from django.db import models

# Create your models here.
class contacts(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False, unique=True)
    email=models.EmailField(unique=True)
    time=models.TimeField(auto_now_add=True)
    notes=models.CharField(null=True,blank=True, max_length=200)
    
    def __str__(self) :
        return self.name