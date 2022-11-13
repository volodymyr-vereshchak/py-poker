from rest_framework import serializers

from poker.models import (
    Table,
    Level,
    Struct,
    Hand,
    Card,
    River,
    Turn,
    Flop,
    PreFlop,
    GameSession
)


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class StructSerializer(serializers.ModelSerializer):
    class Meta:
        model = Struct
        fields = "__all__"


class HandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hand
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class PreFlopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreFlop
        fields = "__all__"


class FlopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flop
        fields = "__all__"


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = "__all__"


class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        fields = "__all__"


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = "__all__"
