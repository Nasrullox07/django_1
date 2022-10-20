from django.db import models

# Create your models here.

class Work(models.Model):
    nomi=models.CharField(max_length=33)
    manzil=models.CharField(max_length=111)
    rasm=models.ImageField(upload_to='media')
    xona1=models.IntegerField()
    xona2=models.IntegerField()
    kv=models.FloatField()
    narx_old=models.IntegerField()
    narx_new=models.IntegerField()

class Clients(models.Model):
    ismi = models.CharField(max_length=30)
    ishi=models.CharField(max_length=111)
    men_haqimda=models.CharField(max_length=111)
    rasm = models.ImageField(upload_to='media')

class Agents(models.Model):
    name = models.CharField(max_length=30)
    mulki = models.CharField(max_length=30)
    rasm=models.ImageField(upload_to='media')

class Oxirgi_ishlar(models.Model):
    rasm=models.ImageField(upload_to='media')
    malumot=models.CharField(max_length=11111111111111111111111111)
    sana=models.DateTimeField(auto_now=True)

class Murojaat(models.Model):
    ism= models.CharField(max_length=50)
    mail= models.EmailField(max_length=50)
    sub= models.CharField(max_length=50)
    mess= models.TextField()
    vaqt= models.DateTimeField(auto_now=True)