import json

from ckeditor_uploader.forms import SearchForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from accommodation.models import Accommodation, Category, Room, Image, Comment
from content.models import Content
from home.forms import SearchForm, RegisterForm
from home.models import Settings, ContactForm, ContactFormMessage, UserProfile, Faq


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata = Accommodation.objects.all()[:4]
    category = Category.objects.all()
    accommodations = Accommodation.objects.all().order_by('-id')[:6]
    lastContent = Content.objects.all().order_by('-id')[:3]
    comments = Comment.objects.filter(publish='True')

    context = {'page': 'home',
               'setting': setting,
               'category': category,
               'accommodations': accommodations,
               'sliderdata': sliderdata,
               'lastContent': lastContent,
               'comments': comments,
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    if current_user.is_active:
        current_user = UserProfile.objects.get(user_id=current_user.id);
    context = {'setting': setting,
               'category': category,
               'current_user': current_user,
               'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    if current_user.is_active:
        current_user = UserProfile.objects.get(user_id=current_user.id);
    context = {'setting': setting,
               'category': category,
               'current_user': current_user,
               'page': 'referanslar'}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    current_user = request.user
    if current_user.is_active:
        current_user = UserProfile.objects.get(user_id=current_user.id);
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
               'current_user': current_user,
               'form': form}
    return render(request, 'iletisim.html', context)


def category_accommodations(request, id, slug):
    current_user = request.user
    if current_user.is_active:
        current_user = UserProfile.objects.get(user_id=current_user.id);
    setting = Settings.objects.get(pk=1)
    categorydata = Category.objects.get(pk=id)
    accommodations = Accommodation.objects.filter(category_id=id)
    category = Category.objects.all()
    context = {'setting': setting,
               'accommodations': accommodations,
               'category': category,
               'categoryData': categorydata,
               'current_user': current_user,
               'page': 'konaklama'}
    return render(request, 'accommodation.html', context)


def accommodation_detail(request, id, slug):
    current_user = request.user
    if current_user.is_active:
        current_user = UserProfile.objects.get(user_id=current_user.id);
    setting = Settings.objects.get(pk=1)
    accommodation = Accommodation.objects.get(pk=id)
    rooms = Room.objects.filter(hotel_id=id)
    images = Image.objects.filter(hotel_id=id)
    comments = Comment.objects.filter(hotel_id=id, status='True')
    category = Category.objects.all()
    context = {'setting': setting,
               'current_user': current_user,
               'accommodation': accommodation,
               'category': category,
               'rooms': rooms,
               'images': images,
               'comments': comments,
               'page': 'konaklama'}
    return render(request, 'accommodation_detail.html', context)


def accommodation_search(request):
    current_user = request.user
    if current_user.is_active:
        current_user = UserProfile.objects.get(user_id=current_user.id);
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
                'current_user': current_user,
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Kullanıcı adı veya şifre yanlış.")
            return HttpResponseRedirect('/login')
    setting = Settings.objects.get(pk=1)
    bimage = Accommodation.objects.get(pk=1)
    context = {
        'setting': setting,
        'bimage': bimage,
    }
    return render(request, 'login.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()
            return HttpResponseRedirect('/')

    form = RegisterForm()
    setting = Settings.objects.get(pk=1)
    bimage = Accommodation.objects.get(pk=1)
    context = {
        'setting': setting,
        'bimage': bimage,
        'form': form,
    }
    return render(request, 'register.html', context)


def faq(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    faq = Faq.objects.filter(status='True').order_by('ordernumber')
    context = {
        'page': 'faq',
        'setting': setting,
        'category': category,
        'faq': faq
    }
    return render(request, 'faq.html', context)
