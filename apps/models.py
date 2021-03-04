from django.db import models

# Create your models here.
class SingerModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class SongModel(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(SingerModel, on_delete=models.CASCADE, related_name='song')

    def __str__(self):
        return self.title