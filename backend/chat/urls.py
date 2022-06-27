from django.urls import path,include
from chat import views
from django.contrib.auth import views as vi
from django.urls import reverse_lazy
app_name = 'chat'
urlpatterns = [
    path('', views.base, name='index'),
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
]