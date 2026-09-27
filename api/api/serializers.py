from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'developer', 'publisher', 'rating', 'maturity_rating']