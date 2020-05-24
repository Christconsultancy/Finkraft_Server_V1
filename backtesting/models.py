from django.db import models
import datetime

STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
)


# Create your models here.
class Statergies(models.Model):
    statergy_name = models.CharField(max_length=255, blank=False, null=False)
    statergy_status = models.CharField(max_length=50, choices=STATUS, default="ACTIVE")

    def __str__(self):
        return self.statergy_name
