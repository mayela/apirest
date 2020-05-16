from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=50)
    specie = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'The pet is a {self.specie} and their name {self.name}'
