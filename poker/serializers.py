from rest_framework import serializers

from poker.models import Table, Level, Struct, Hand, Card, River, Turn, Flop, PreFlop, GameSession


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level


class StructSerializer(serializers.ModelSerializer):
    class Meta:
        model = Struct


class HandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hand


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card


class PreFlopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreFlop


class FlopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flop


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn


class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
