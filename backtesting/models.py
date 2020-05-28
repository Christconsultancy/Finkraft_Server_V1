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


class Stock(models.Model):
    stock_name = models.CharField(max_length=50, blank=False, null=True, unique=True)

    def __str__(self):
        return self.stock_name


class TestResult(models.Model):
    stock_id = models.ForeignKey(Stock, blank=False, null=False,on_delete=models.CASCADE)
    test_date = models.DateTimeField(default=datetime.date.today)
    test_start_date = models.DateTimeField(blank=False, null=False)
    test_end_date = models.DateTimeField(blank=False, null=False)
    test_timeframe = models.IntegerField(blank=False, null=False)
    test_result_target = models.CharField(max_length=15, blank=False, null=False)
    test_result_entry = models.CharField(max_length=15, blank=False, null=False)
    test_result_stockloss = models.CharField(max_length=15, blank=False, null=False)
