from django.db import models

import datetime


class Sector(models.Model):
    sector = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.sector}"


class Industry(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry = models.CharField(max_length=60)

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


class CryptoCurrency(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
