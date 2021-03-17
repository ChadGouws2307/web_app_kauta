from django.db import models
from django.contrib.auth.models import User

import datetime


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=8)
    no_of_shares = models.IntegerField(blank=False, help_text='Number of Shares in Trade')
    date = models.DateTimeField(blank=False, default=datetime.datetime.today(), help_text='Date of Trade')
    price = models.FloatField(blank=False, help_text='Price at which Trade was Made')

    class Meta:
        ordering = ['date', 'ticker']

    def __str__(self):
        return f"{self.ticker}, {self.date}"


class TradeFile(models.Model):
    trade_file = models.FileField(upload_to='documents/')
