from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username
