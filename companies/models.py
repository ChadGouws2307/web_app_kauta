from django.db import models

import datetime


class Sector(models.Model):
    sector = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.sector}"


class Industry(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.industry}, {self.sector}"


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country_name}"


class CompanyStock(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    listed_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class CompanyFinancials(models.Model):
    company_name = models.ForeignKey(CompanyStock, on_delete=models.CASCADE, blank=False)
    period_ending = models.DateField(default=datetime.date(1658, 1, 1), blank=False)
    year = models.IntegerField(blank=False)

    report_period_length = (
        ('f', 'Full Year'),
        ('h', 'Half Year'),
        ('q', 'Quarterly')
    )

    full_half_quarter = models.CharField(max_length=1, choices=report_period_length, blank=False,
                                         help_text='Length of Reporting Period')
    currencies = (
        ('usd', 'USD'),
        ('zar', 'ZAR'),
        ('gbp', 'GBP')
    )
    reporting_currency = models.CharField(max_length=3, choices=currencies, blank=True, help_text='Reporting Currency')
    revenue = models.IntegerField(blank=True, help_text='In Billions')
    cost_of_sales = models.IntegerField(blank=True, help_text='In Billions')
    gross_profit = models.IntegerField(blank=True, help_text='In Billions')
    net_profit = models.IntegerField(blank=True, help_text='In Billions')

    def __str__(self):
        return f"{self.company_name}, {self.full_half_quarter}, {self.period_ending}"
