# Generated by Django 3.2.6 on 2021-10-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bateria', models.FloatField(default=0)),
                ('serial', models.CharField(max_length=100)),
            ],
        ),
    ]
