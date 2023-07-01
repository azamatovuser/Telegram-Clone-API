from django.db import models


class Friend(models.Model):
    account = models.OneToOneField('account.Account', on_delete=models.CASCADE, null=True, blank=True)