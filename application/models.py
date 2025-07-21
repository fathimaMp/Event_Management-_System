from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='venue_images/')

    def __str__(self):
        return f"{self.name} ({self.code})"


