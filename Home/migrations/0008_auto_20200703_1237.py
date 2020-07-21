# Generated by Django 2.2.5 on 2020-07-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200703_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Level',
            field=models.CharField(blank=True, choices=[('Juniour', 'Junior'), ('Intermediate', 'Intermediate'), ('Ivy', 'Ivy'), ('Senior', 'Senior')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('sw', 'Take Account'), ('OW', 'Transcribing Account'), ('s', 'Bidding Account')], max_length=2),
        ),
    ]