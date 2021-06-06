from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Team, Player, Game


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.ReadOnlyField(source="team.name")
    team_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

