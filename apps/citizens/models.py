from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Citizen(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    kind = models.ForeignKey(AnimalKind, on_delete=models.PROTECT, related_name='citizens')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'.strip()
