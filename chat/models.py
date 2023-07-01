from django.db import models
from account.models import Account


class Friend(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)