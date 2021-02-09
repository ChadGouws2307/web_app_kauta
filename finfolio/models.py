from django.db import models
from django.contrib.auth.models import User

import datetime

from companies.models import CompanyStock


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyStock, blank=False, on_delete=models.CASCADE, help_text='Company Stock')
    no_of_shares = models.IntegerField(blank=False, help_text='Number of Shares in Trade')
    date = models.DateTimeField(blank=False, default=datetime.datetime.today(), help_text='Date of Trade')
    price = models.FloatField(blank=False, help_text='Price at which Trade was Made')

    class Meta:
        ordering = ['date', 'company']

    def __str__(self):
        return f"{self.company}, {self.date}, {self.no_of_shares}"
