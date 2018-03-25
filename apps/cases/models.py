from django.db import models
from model_utils import Choices


class Case(models.Model):
    DANGER_LEVEL = Choices('safe', 'minor', 'considerable', 'high', 'very_high')

    title = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    citizens = models.ManyToManyField('citizens.Citizen')
    danger_level = models.CharField(choices=DANGER_LEVEL, max_length=12)

    def __str__(self) -> str:
        return f'{self.title}: {self.danger_level}'
