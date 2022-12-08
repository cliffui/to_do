from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class List(models.Model):
    user=models.ForeignKey(User,related_name="lists",on_delete=models.DO_NOTHING)
    body=models.CharField(max_length=140)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user}"
            f"{self.body}"
            f"({self.created_at:%Y-%m-%d})"
        )