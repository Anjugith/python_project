# Generated by Django 4.2 on 2024-02-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmovieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
