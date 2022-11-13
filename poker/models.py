from django.db import models


# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=64)
    buy_in = models.PositiveIntegerField()
    chips = models.PositiveIntegerField()



class GameSession(models.Model):
    table = models.ForeignKey()