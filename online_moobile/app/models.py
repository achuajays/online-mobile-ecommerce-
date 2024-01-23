from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    img = models.ImageField( upload_to='media', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)


class verify(models.Model):
    img = models.ImageField( upload_to='media', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)



class exchange(models.Model):
    img = models.ImageField( upload_to='img', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)


class service(models.Model):
    model = models.CharField( max_length=1000)
    problem = models.CharField( max_length=1000)


class chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_f = models.CharField( max_length=1000)
    t =   models.CharField( max_length=1000)

