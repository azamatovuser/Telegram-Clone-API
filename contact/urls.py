from django.urls import path
from .views import ContactList, ContactCreate

urlpatterns = [
    path('contac-list/', ContactList.as_view()),
    path('contact-create/', ContactCreate.as_view())
]