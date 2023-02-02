from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    business = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.first_name + '' + self.last_name
    
    