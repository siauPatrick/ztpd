import factory.fuzzy

from citizens import models


class SpeciesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Species

    name = factory.fuzzy.FuzzyText(prefix='species', length=50)


class CitizenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Citizen

    name = factory.Faker('name')
    species = factory.SubFactory(SpeciesFactory)
    gender = factory.fuzzy.FuzzyChoice(models.Citizen.GENDER)
    photo_url = factory.fuzzy.FuzzyText(prefix='https://zootopia.com/images/', length=50)
    fandom_url = factory.LazyAttribute(lambda obj: f'http://zootopia.wikia.com/wiki/{obj.name}')
