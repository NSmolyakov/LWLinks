from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]


class Link(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    read = models.BooleanField()
    watch = models.BooleanField()

    def __str__(self):
        return self.title
