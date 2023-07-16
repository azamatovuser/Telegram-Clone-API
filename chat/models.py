from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=221)
    account = models.ManyToManyField('account.Account', related_name='room_account')


class Message(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='message_account')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='message')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account}'s message in {self.room}"
