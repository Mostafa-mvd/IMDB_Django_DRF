# Generated by Django 4.0.4 on 2022-05-02 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies_post', '0014_alter_movie_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 2, 20, 9, 52, 660101, tzinfo=utc)),
        ),
    ]
