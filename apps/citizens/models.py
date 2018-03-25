from django.db import models
from model_utils import Choices


class Species(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Citizen(models.Model):
    GENDER = Choices('male', 'female')

    name = models.CharField(max_length=150)
    species = models.ForeignKey(Species, on_delete=models.PROTECT, related_name='citizens')
    gender = models.CharField(choices=GENDER, max_length=6)
    photo_url = models.URLField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
