from django.db import models

# Create your models here.


class Link(models.Model):
    title = models.CharField(max_length=120)
    number = models.PositiveSmallIntegerField()
    link = models.URLField()
    read = models.BooleanField()
    watch = models.BooleanField()

    def __str__(self):
        return self.title
