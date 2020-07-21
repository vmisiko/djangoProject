# Generated by Django 2.2.5 on 2020-07-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20200711_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Level',
            field=models.CharField(blank=True, choices=[('Senior', 'Senior'), ('Ivy', 'Ivy'), ('Juniour', 'Junior'), ('Intermediate', 'Intermediate')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('sw', 'Take Account'), ('OW', 'Transcribing Account'), ('s', 'Bidding Account')], max_length=2),
        ),
    ]