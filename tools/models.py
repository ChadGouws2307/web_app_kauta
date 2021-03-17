from django.db import models


class PCAFile(models.Model):
    no_of_components = models.PositiveIntegerField()
    pca_file = models.FileField(upload_to='documents/')
