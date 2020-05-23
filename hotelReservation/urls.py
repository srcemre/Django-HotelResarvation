"""hotelReservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('accommodation/', include('accommodation.urls')),
    path('user/', include('user.urls')),
    path('reservation/',include('reservation.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('category/<int:id>/<slug:slug>/', views.category_accommodations, name='category_accommodations'),
    path('accommodation/<int:id>/<slug:slug>/', views.accommodation_detail, name='accommodation_detail'),
    path('search/',views.accommodation_search, name='product_search'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('search_auto/',views.accommodation_search_auto, name='accommodation_search_auto'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
