from django.db import models

# Create your models here.
class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title       = models.CharField(max_length=150)
    keywords    = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company     = models.CharField(max_length=255)
    address     = models.TextField(blank=True,max_length=255)
    phone       = models.CharField(blank=True,max_length=255)
    fax         = models.CharField(blank=True,max_length=255)
    email       = models.CharField(blank=True,max_length=255)
    smtpserver  = models.CharField(max_length=20)
    smtpemail   = models.CharField(max_length=20)
    smtppassword= models.CharField(max_length=10)
    smtpport    = models.CharField(max_length=5)
    icon        = models.ImageField(blank=True,upload_to='images/')
    facebook    = models.CharField(blank=True,max_length=50)
    instagram   = models.CharField(blank=True,max_length=50)
    twitter     = models.CharField(blank=True,max_length=50)
    aboutus     = models.TextField(blank=True)
    references  = models.TextField(blank=True)
    contact     = models.TextField(blank=True)
    status      = models.CharField(max_length=10, choices=STATUS)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title