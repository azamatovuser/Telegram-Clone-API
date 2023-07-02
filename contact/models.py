from django.db import models



class Contact(models.Model):
    author = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"contact of {self.name} in {self.author}"



