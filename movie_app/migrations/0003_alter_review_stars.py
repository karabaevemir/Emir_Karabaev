# Generated by Django 4.1.5 on 2023-01-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, 'Bad (1)'), (2, 'So so (2)'), (3, 'Good (3)'), (4, 'Nice (4)'), (5, 'Great (5)')], default=5),
        ),
    ]
