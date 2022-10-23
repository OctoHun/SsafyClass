# Generated by Django 3.2.11 on 2022-10-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actor_movies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_data',
            new_name='release_date',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
    ]