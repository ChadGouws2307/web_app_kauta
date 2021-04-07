from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    email = models.EmailField()
    permission = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"


class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)
    email_marketing = models.BooleanField(default=False)
    product_launch_and_updates = models.BooleanField(default=False)
    investing_ideas = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"
