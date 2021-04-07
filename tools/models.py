from django.db import models


class CorrFile(models.Model):
    corr_file = models.FileField(upload_to='documents/')
