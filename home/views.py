import json

from ckeditor_uploader.forms import SearchForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from accommodation.models import Accommodation, Category, Room, Image, Comment
from home.forms import SearchForm
from home.models import Settings, ContactForm, ContactFormMessage


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata = Accommodation.objects.all()[:4]
    category = Category.objects.all()
    accommodations = Accommodation.objects.all()[6::-1]  # Son girilenleri listeliyor.
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'accommodations': accommodations,
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


def accommodation_detail(request, id, slug):
    setting = Settings.objects.get(pk=1)
    accommodation = Accommodation.objects.get(pk=id)
    rooms = Room.objects.filter(hotel_id=id)
    images = Image.objects.filter(hotel_id=id)
    comments = Comment.objects.filter(hotel_id=id, status='True')
    category = Category.objects.all()
    context = {'setting': setting,
               'accommodation': accommodation,
               'category': category,
               'rooms': rooms,
               'images': images,
               'comments': comments,
               'page': 'konaklama'}
    return render(request, 'accommodation_detail.html', context)


def accommodation_search(request):
    if request.method == 'POST':  # form post edildiyse
        form = SearchForm(request.POST)
        if form.is_valid():
            setting = Settings.objects.get(pk=1)
            category = Category.objects.all()
            query = form.cleaned_data['query']  # formdan bilgiyi al
            catid = form.cleaned_data['catid']
            if catid == 0:
                accommodations = Accommodation.objects.filter(title__icontains=query)
                # select * from accom... where title like %query%
            else:
                accommodations = Accommodation.objects.filter(title__icontains=query, category_id=catid)
            context = {
                'setting': setting,
                'accommodations': accommodations,
                'category': category,
                'page': 'konaklama'
            }
            return render(request, 'accommodation_search.html', context)

    return HttpResponseRedirect('/')


def accommodation_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        accommodation = Accommodation.objects.filter(title__icontains=q)
        results = []
        for rs in accommodation:
            accommodation_json = {}
            accommodation_json = rs.title
            results.append(accommodation_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
