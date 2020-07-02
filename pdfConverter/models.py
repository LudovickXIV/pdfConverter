from django.db import models

class Converter(models.Model):
    html = models.FileField()
    # css = models.FileField(name="fileToUploadHTML")