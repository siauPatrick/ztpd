from django.db import models
from model_utils import Choices


class Case(models.Model):
    title = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    citizens = models.ManyToManyField('citizens.Citizen')
    danger_level = Choices('safe', 'minor', 'considerable', 'high', 'very_high')

    def __str__(self) -> str:
        return f'{self.title}: {self.danger_level}'
