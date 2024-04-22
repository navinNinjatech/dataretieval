from django.db import models

class Event(models.Model):

    """
    Represents an event.

    Attributes:
        id (CharField): The primary key for the Event model.
        title (CharField): The title of the event.
        start_date (DateTimeField): The start date of the event.
        start_time (TimeField): The start time of the event.
        end_date (DateTimeField): The end date of the event.
        end_time (TimeField): The end time of the event.
        min_price (DecimalField): The minimum price of the event.
        max_price (DecimalField): The maximum price of the event.
    """

    # Primary key for the Event model
    id = models.CharField(max_length=100, primary_key=True)

     # Title of the event
    title = models.CharField(max_length=100)

    # Start date and time of the event
    start_date = models.DateTimeField()
    start_time = models.TimeField()

    # End date and time of the event
    end_date = models.DateTimeField()
    end_time = models.TimeField()

    # Minimum and maximum price of the event
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
