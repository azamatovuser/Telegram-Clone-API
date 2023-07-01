from django.urls import path
from .views import RoomListCreateAPIView, RoomWithMessageAPIView


urlpatterns = [
    path('rooms/', RoomListCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomWithMessageAPIView.as_view()),
]