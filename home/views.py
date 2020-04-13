from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from accommodation.models import Accommodation, Category, Room, Image
from home.models import Settings, ContactForm, ContactFormMessage


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata = Accommodation.objects.all()[:4]
    category = Category.objects.all()
    accommodations = Accommodation.objects.all()[6::-1] #Son girilenleri listeliyor.
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'accommodations':accommodations,
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'referanslar'}
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
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'iletisim',
               'category': category,
               'form': form}
    return render(request, 'iletisim.html', context)


def category_accommodations(request, id, slug):
    setting = Settings.objects.get(pk=1)
    categorydata = Category.objects.get(pk=id)
    accommodations = Accommodation.objects.filter(category_id=id)
    category = Category.objects.all()
    context = {'setting': setting,
               'accommodations': accommodations,
               'category': category,
               'categoryData': categorydata,
               'page': 'konaklama'}
    return render(request, 'accommodation.html', context)


def accommodation_detail(request,id,slug):
    setting = Settings.objects.get(pk=1)
    accommodation = Accommodation.objects.get(pk=id)
    rooms = Room.objects.filter(hotel_id = id)
    images = Image.objects.filter(hotel_id = id)
    category = Category.objects.all()
    context = {'setting': setting,
               'accommodation': accommodation,
               'category': category,
               'rooms':rooms,
               'images':images,
               'page': 'konaklama'}
    return render(request, 'accommodation_detail.html', context)