from django.conf import settings
from django.db import models


# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=64)
    buy_in = models.PositiveIntegerField()
    chips = models.PositiveIntegerField()


class Level(models.Model):
    level = models.PositiveIntegerField()
    small_blind = models.PositiveIntegerField()
    big_blind = models.PositiveIntegerField()
    min_limit = models.PositiveIntegerField()
    max_limit = models.PositiveIntegerField()
    ante = models.PositiveIntegerField()


class Struct(models.Model):
    name = models.CharField(max_length=64)
    level = models.ManyToManyField(Level)


class Hand(models.Model):
    played_at = models.DateTimeField(auto_now=True)
    hand_num = models.PositiveIntegerField()


class Card(models.Model):
    class CardsDenomination(models.IntegerChoices):
        TWO = 0
        THREE = 1
        FOUR = 2
        FIVE = 3
        SIX = 4
        SEVEN = 5
        EIGHT = 6
        NINE = 7
        TEN = 8
        JACK = 9
        QUIN = 10
        KING = 11
        ACE = 12

    class CardSuit(models.IntegerChoices):
        HEART = 0
        DIAMOND = 1
        CROSS = 2
        SPADE = 3

    card_denomination = models.IntegerField(choices=CardsDenomination)
    card_suit = models.IntegerField(choices=CardSuit)


class Action(models.IntegerChoices):
    BET = 0
    FOLD = 1


class Order(models.Model):
    hand = models.ForeignKey(Hand, on_delete=models.CASCADE)
    card1 = models.ForeignKey(Card, on_delete=models.CASCADE)
    action = models.IntegerField(choices=Action)
    bet = models.IntegerField(blank=True, null=True)


class PreFlop(Order):
    card2 = models.ForeignKey(Card, on_delete=models.CASCADE)


class Flop(Order):
    card2 = models.ForeignKey(Card, on_delete=models.CASCADE)
    card3 = models.ForeignKey(Card, on_delete=models.CASCADE)


class Turn(Order):
    pass


class River(Order):
    pass


class GameSession(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    struct = models.ForeignKey(Struct, on_delete=models.CASCADE)
    next_level_hands = models.PositiveIntegerField()