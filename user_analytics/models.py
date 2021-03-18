from django.db import models


class UserPageView(models.Model):
    user = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    template = models.CharField(max_length=150)
