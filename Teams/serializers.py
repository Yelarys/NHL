from rest_framework import serializers
from .models import Team, Player
from django.contrib.auth.models import User

class TeamModelSerializer(serializers.ModelSerializer):
   class Meta:
        model = Team
        fields = ('id', 'name', 'acronym', 'conference', 'titles')

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class PlayerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'country', 'position', 'team')
