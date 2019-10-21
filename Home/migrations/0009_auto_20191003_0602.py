# Generated by Django 2.2.5 on 2019-10-03 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20191003_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('sw', 'Take Account'), ('s', 'Bidding Account'), ('OW', 'Transcribing Account')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('S', 'secondary'), ('P', 'primary')], max_length=1),
        ),
    ]
