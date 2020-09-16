from django.db import models

# Create your models here.
class Jam(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tempo = models.IntegerField()
    notes = models.CharField(max_length=100)
    bassDrumNotes = models.CharField(max_length=100)
    cymbalNotes = models.CharField(max_length=100)
    snareNotes = models.CharField(max_length=100)

    def __str__(self):
        return self.username