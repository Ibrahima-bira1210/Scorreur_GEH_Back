from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from backend.api.models import Player, Team, Game
from backend.api.serializers import UserSerializer, GroupSerializer, GameSerializer, TeamSerializer, PlayerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('id')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('id')
    serializer_class = PlayerSerializer
    permissions_classes = [permissions.IsAuthenticated]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('id')
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
