# Generated by Django 2.2.12 on 2020-07-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20200717_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_form',
            name='degree',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='data_form',
            name='program',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
