from django.db import models

class Event(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    start_time = models.TimeField()
    end_date = models.DateTimeField()
    end_time = models.TimeField()
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
