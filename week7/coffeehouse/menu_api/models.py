from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()

class Special(models.Model):
    name = models.CharField(max_length=48)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    @property
    def calorie_count(self):
        return sum(self.ingredients.all().values_list("calories", flat=True))

#('menu_api.Ingredient')
