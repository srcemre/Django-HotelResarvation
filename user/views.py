from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from accommodation.models import Category, Comment
from content.models import Content, ContentForm, ContentImageForm, CImages
from home.models import Settings, UserProfile
from reservation.models import Reservation, ReservationRoom
from user.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url='/login')
def index(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    current_user = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'setting': setting,
        'category': category,
        'current_user': current_user,
    }
    return render(request, 'userprofile.html', context)


@login_required(login_url='/login')
def update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Hesabın başarıyla güncellendi.')
            return redirect('/user')
    else:
        setting = Settings.objects.get(pk=1)
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'setting': setting,
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifren başarıyla değiştirildi.')
            return redirect('password')
        else:
            messages.error(request, 'Bilgileri doğru giriniz.')
    else:
        setting = Settings.objects.get(pk=1)
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {
            'setting': setting,
            'category': category,
            'form': form,
        }
        return render(request, 'change_password.html', context)


@login_required(login_url='/login')
def reservation(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    reservations = Reservation.objects.filter(user_id=request.user.id).order_by('-create_at')
    context = {
        'setting': setting,
        'category': category,
        'reservations': reservations,
    }
    return render(request, 'user_reservations.html', context)


@login_required(login_url='/login')
def reservationdetail(request, id):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    reservation = Reservation.objects.get(user_id=request.user.id, id=id)
    reservationdetail = ReservationRoom.objects.filter(reservation_id=id)
    context = {
        'setting': setting,
        'category': category,
        'reservationdetail': reservationdetail,
    }
    return render(request, 'user_reservations_detail.html', context)


@login_required(login_url='/login')
def comments(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    comments = Comment.objects.filter(user_id=request.user.id).order_by('create_at')
    context = {
        'setting': setting,
        'category': category,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomments(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorumunuz Silindi.')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def contents(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    contents = Content.objects.filter(user_id=request.user.id).order_by('create_at')
    context = {
        'setting': setting,
        'category': category,
        'contents': contents,
    }
    return render(request, 'user_contents.html', context)


@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.thumbnail = form.cleaned_data['thumbnail']
            data.type = form.cleaned_data['type']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'İçeriğin başarıyla eklendi.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.warning(request, 'Content Form Hata:' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        setting = Settings.objects.get(pk=1)
        category = Category.objects.all()
        form = ContentForm()
        context = {
            'setting': setting,
            'category': category,
            'form': form,
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login')
def contentedit(request, id):
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'İçeriğiniz başarıyla güncellendi.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.warning(request, 'Content Form Hata:' + str(form.errors))
            return HttpResponseRedirect('/user/contentedit' + str(id))
    else:
        setting = Settings.objects.get(pk=1)
        category = Category.objects.all()
        form = ContentForm(instance=content)
        context = {
            'setting': setting,
            'category': category,
            'form': form,
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login')
def deletecontent(request, id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'İçeriğiniz başarıyla Silindi.')
    return HttpResponseRedirect('/user/contents/')


@login_required(login_url='/login')
def contentaddimage(request, id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = ContentImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = CImages()
            data.title = form.cleaned_data['title']
            data.content_id = id
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, 'Resminiz başarıyla karşıya yüklendi.')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Form Hata: ' + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        content = Content.objects.get(id=id)
        images = CImages.objects.filter(content_id=id)
        form = ContentImageForm()
        context = {
            'content': content,
            'images': images,
            'form': form,
        }
        return render(request, 'user_content_gallary.html', context)


@login_required(login_url='/login')
def contentdeleteimage(request, id):
    lasturl = request.META.get('HTTP_REFERER')
    CImages.objects.filter(id=id).delete()
    messages.success(request, 'Resim başarıyla Silindi.')
    return HttpResponseRedirect(lasturl)
