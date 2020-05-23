from django import forms


class RezarvasyonForm(forms.Form):
    roomid = forms.IntegerField()
    person = forms.IntegerField()
    checkin = forms.DateTimeField()
    checkout = forms.DateTimeField()


class ReservationConfirmForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    total = forms.FloatField()

    checkin = forms.CharField()
    checkout = forms.CharField()
    person = forms.IntegerField()
    price = forms.FloatField()
    roomid = forms.FloatField()
