# Generated by Django 4.1.5 on 2023-01-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]
