# Generated by Django 3.0.5 on 2021-05-24 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210522_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='team_a_state',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='game',
            name='team_b_state',
        ),
    ]
