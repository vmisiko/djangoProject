# Generated by Django 2.2.5 on 2020-06-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200625_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Level',
            field=models.CharField(blank=True, choices=[('r', 'Seni0r'), ('Ivy', 'Ivy'), ('Intermediate', 'Intermediate'), ('Juniour', 'Junior')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('sw', 'Take Account'), ('OW', 'Transcribing Account'), ('s', 'Bidding Account')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=1),
        ),
    ]
