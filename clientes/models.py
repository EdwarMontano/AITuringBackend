
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProfileCliente(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    name_cliente=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    is_admin =models.BooleanField(default=False)

    user_created=models.DateTimeField(auto_now_add=True)
    user_modifed=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username

     
     

