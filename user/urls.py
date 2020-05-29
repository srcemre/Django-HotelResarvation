from django.urls import path

from user import views

urlpatterns = [
    path('', views.index, name='userpage'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),

    path('reservations/', views.reservation, name='reservation'),
    path('reservationdetail/<int:id>', views.reservationdetail, name='reservationdetail'),

    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomments, name='deletecomments'),

    path('contents/', views.contents, name='contents'),
    path('contentadd/', views.addcontent, name='addcontent'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.deletecontent, name='deletecontent'),
    path('contentaddimage/<int:id>', views.contentaddimage, name='contentaddimage'),
    path('contentdeleteimage/<int:id>', views.contentdeleteimage, name='contentdeleteimage'),
]
