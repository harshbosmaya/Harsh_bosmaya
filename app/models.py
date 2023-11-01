from django.db import models

# Create your models here.
class contacts(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    time=models.TimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name