# Generated by Django 4.0.4 on 2022-05-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_post', '0006_moviecrew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='duration_sec',
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
