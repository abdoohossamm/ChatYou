from django.urls import path

from oto.api import views

urlpatterns = [
    path('', views.ChatList.as_view()),
    path('create/', views.ChatCreate.as_view()),
    path('<int:pk>', views.ChatDetail.as_view())
]