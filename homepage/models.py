from django.db import models

# Create your models here.

class DernierPublication(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='dernierpublications')
    date = models.DateTimeField(auto_now=True)
    par = models.CharField(max_length=150, default="Admin")
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.name


class Imagepricipale(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='imagespricipale')
    
    def __str__(self):
        return self.name
    
class Entete(models.Model):
    image = models.ImageField(upload_to='entête')
    titre1 = models.TextField()
    titre2 = models.TextField()
    
    def __str__(self):
        return self.titre1
class Menbre(models.Model):
    name = models.CharField(max_length=150)
    domaine = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="menbres")
    facebook = models.CharField(max_length=350)
    whatsapp = models.CharField(max_length=350)
    phone = models.CharField(max_length=200)
    fonction = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    titre = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to="blog")
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.titre
    

