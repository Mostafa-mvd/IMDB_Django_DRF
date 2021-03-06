# Generated by Django 4.0.4 on 2022-05-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_post', '0009_alter_moviecast_unique_together_alter_movie_title_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='moviecast',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='moviecast',
            name='character_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='moviecast',
            unique_together={('person_name', 'movie', 'character_name')},
        ),
        migrations.AlterUniqueTogether(
            name='moviecrew',
            unique_together={('person_name', 'movie')},
        ),
    ]
