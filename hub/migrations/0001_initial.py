# Generated by Django 3.2.6 on 2021-10-14 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurante', '0002_alter_restaurante_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direcccion', models.CharField(max_length=150)),
                ('restaurante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='restaurante.restaurante')),
            ],
        ),
    ]