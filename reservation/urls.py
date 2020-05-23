from django.urls import path

from reservation import views

urlpatterns = [
    path('details/', views.reservation, name="reservation"),
    path('confirm/', views.reservationConfirm, name="reservationConfirm"),

]
