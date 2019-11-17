# Generated by Django 2.2.5 on 2019-11-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0040_auto_20191114_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Level',
            field=models.CharField(blank=True, choices=[('Intermediate', 'Intermediate'), ('Ivy', 'Ivy'), ('Juniour', 'Junior'), ('r', 'Seni0r')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('s', 'Bidding Account'), ('sw', 'Take Account'), ('OW', 'Transcribing Account')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('P', 'primary'), ('S', 'secondary')], max_length=1),
        ),
    ]
