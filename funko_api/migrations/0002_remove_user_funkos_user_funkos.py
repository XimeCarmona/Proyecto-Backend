# Generated by Django 5.0.3 on 2024-06-06 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='funkos',
        ),
        migrations.AddField(
            model_name='user',
            name='funkos',
            field=models.ManyToManyField(to='funko_api.funko'),
        ),
    ]