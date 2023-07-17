from django.urls import path
from .views import ContactListAPIView, ContactRUDAPIView, ContactCreateAPIView

urlpatterns = [
    path('list/', ContactListAPIView.as_view()),
    # path('generic/', ContactCreateGenericAPIView.as_view()),
    path('create/', ContactCreateAPIView.as_view()),
    path('rud/<int:pk>/', ContactRUDAPIView.as_view()),
]
