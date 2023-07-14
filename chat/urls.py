from django.urls import path
from .views import RoomListCreateAPIView, RoomWithMessageAPIView, MessageCreateAPIView, lobby


urlpatterns = [
    path('rooms/', RoomListCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomWithMessageAPIView.as_view()),
    path('rooms/message/create/', MessageCreateAPIView.as_view()),
    path('', lobby)
]