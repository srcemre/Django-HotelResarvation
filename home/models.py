from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.forms import ModelForm, TextInput


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
    aboutus     = RichTextUploadingField(blank=True)
    references  = RichTextUploadingField(blank=True)
    contact     = RichTextUploadingField(blank=True)
    status      = models.CharField(max_length=10, choices=STATUS)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name      = models.CharField(blank=True, max_length=20)
    email     = models.CharField(blank=True, max_length=50)
    subject   = models.CharField(blank=True, max_length=50)
    message   = models.CharField(blank=True, max_length=255)
    status    = models.CharField(max_length=10, choices=STATUS, default='New')
    ip        = models.CharField(blank=True, max_length=20)
    note      = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name'    : TextInput(attrs={'class': 'aa-contact-area', 'placeholder': 'Ad & Soyad'}),
            'subject' : TextInput(attrs={'class': 'aa-contact-area', 'placeholder': 'Konu'}),
            'email'   : TextInput(attrs={'class': 'aa-contact-area', 'placeholder': 'E-Posta'}),
            'message' : TextInput(attrs={'class': 'aa-contact-area', 'placeholder': 'Mesaj Yaz'}),
        }