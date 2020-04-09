from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accommodation.models import Accommodation, Category
from home.models import Settings, ContactForm, ContactFormMessage


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata = Accommodation.objects.all()[:4]
    category = Category.objects.all()
    context={'setting':setting,
             'category':category,
             'page':'home',
             'sliderdata':sliderdata }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Settings.objects.get(pk=1)
    context={'setting':setting,
             'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Settings.objects.get(pk=1)
    context={'setting':setting,
             'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Settings.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting,
               'page': 'iletisim',
               'form': form }
    return render(request, 'iletisim.html', context )