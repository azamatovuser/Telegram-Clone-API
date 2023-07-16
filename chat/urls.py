from django.urls import path, include
from rest_framework import routers
from .views import RoomListCreateAPIView, RoomWithMessageAPIView, MessageCreateAPIView, \
    lobby, RoomViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r"rooms", RoomViewSet)
router.register(r"messages", MessageViewSet)

urlpatterns = [
    # http
    path('http/rooms/', RoomListCreateAPIView.as_view()),
    path('http/rooms/<int:pk>/', RoomWithMessageAPIView.as_view()),
    path('http/rooms/message/create/', MessageCreateAPIView.as_view()),

    # simple websocket without database and API
    path('test/', lobby),

    # dynamic websocket with API
    path("ws/", include(router.urls)),
]