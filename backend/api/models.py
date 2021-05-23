from django.db import models
from jsonfield import JSONField


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    mark = models.IntegerField(null=True, blank=True)
    mark_per_match = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/team/log', blank=True)


class Player(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    position = models.IntegerField(db_index=True)
    status = models.BooleanField()
    mark = models.IntegerField(null=True, blank=True)
    mark_per_match = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/players/logo', blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Game(models.Model):
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE)
    score_a = models.IntegerField(null=True, blank=True)
    score_b = models.IntegerField(null=True, blank=True)
    team_a_state = JSONField()
    team_b_state = JSONField()
    date = models.DateField()
