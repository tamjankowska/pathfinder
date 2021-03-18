from django.db import models
from taggit.managers import TaggableManager

class Location(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default = "Unknown")

    def __str__(self):
        return f"{self.name}"

class Phenomena(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    date_of_occ = models.DateField("Date of occurrence")
    image = models.ImageField(upload_to="images/")
    tags = TaggableManager()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description[:30]}... "