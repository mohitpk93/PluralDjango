# Generated by Django 2.2.5 on 2019-09-07 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='secondd_player',
            new_name='second_player',
        ),
    ]
