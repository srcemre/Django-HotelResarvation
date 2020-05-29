from django.urls import path

from content import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/<slug:slug>/', views.content_detail, name='content_detail'),
]
