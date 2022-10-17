from django.urls import path,include
from oto import views
from django.contrib.auth import views as vi
from django.urls import reverse_lazy
app_name = 'oto'
urlpatterns = [
    # path('', views.base, name='index'),
    path('chat/', views.index, name='index'),
    # path('chat/<str:room_name>/', views.room, name='room'),
]