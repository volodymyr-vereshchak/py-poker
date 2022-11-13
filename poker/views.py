from rest_framework import viewsets

from poker.models import GameSession
from poker.serializers import GameSessionSerializer


class GameSessionView(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer
