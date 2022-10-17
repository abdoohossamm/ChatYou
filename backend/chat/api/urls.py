from django.urls import path

from chat.api import views

urlpatterns = [
    path('message/', views.MessageList.as_view()),
    path('message/create/', views.MessageCreate.as_view()),
    path('message/<int:pk>', views.MessageDetail.as_view()),
    path('room/', views.RoomList.as_view()),
    path('room/create/', views.RoomCreate.as_view()),
    path('room/<int:pk>/', views.RoomDetail.as_view())
]