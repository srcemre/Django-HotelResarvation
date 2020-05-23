from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.utils.crypto import get_random_string

from accommodation.models import Category, Room
from home.models import Settings, UserProfile
from reservation.forms import RezarvasyonForm, ReservationConfirmForm
from reservation.models import Reservation, ReservationRoom


@login_required(login_url='/login')
def reservationConfirm(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = ReservationConfirmForm(request.POST)
        if form.is_valid():
            data = Reservation()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = form.cleaned_data['total']
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            detail = ReservationRoom()
            detail.reservation_id = data.id
            detail.room_id = form.cleaned_data['roomid']
            detail.user_id = current_user.id
            detail.checkin = form.cleaned_data['checkin']
            detail.checkout = form.cleaned_data['checkout']
            detail.person = form.cleaned_data['person']
            detail.quantity = 1

            room = Room.objects.get(id=detail.room_id)
            room.amount -= 1
            room.save()

            detail.price = room.price
            detail.amount = room.amount
            detail.save()

            messages.success(request, "Rezervasyonunuz işleminiz başarı ile gerçekleştirildi. Teşekkür Ederiz.")
            context = {
                'setting': setting,
                'category': category,
                'ordercode': ordercode,
            }
            return render(request, "reservation_complated.html", context)

    messages.error(request, form.errors)
    return HttpResponseRedirect('/reservation/details/')


@login_required(login_url='/login')
def reservation(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    current_user = UserProfile.objects.get(user_id=current_user.id);
    if request.method == 'POST':
        form = RezarvasyonForm(request.POST)
        if form.is_valid():
            checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            person = form.cleaned_data['person']
            roomid = form.cleaned_data['roomid']
            room = Room.objects.get(pk=roomid)
            test = checkout - checkin
            price = room.price * test
            context = {'checkin': checkin,
                       'checkout': checkout,
                       'room': room,
                       'person': person,
                       'test': test,
                       'price': price,
                       'setting': setting,
                       'category': category,
                       'current_user': current_user,
                       'page': 'rezervasyonForm'}
            return render(request, "reservation.html", context)
    return HttpResponseRedirect('/reservation/details/')


