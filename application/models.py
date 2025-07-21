from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='venue_images/')

    def __str__(self):
        return f"{self.name} ({self.code})"


class BookingEnquiry(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.venue.name} ({self.start_date} to {self.end_date})"


