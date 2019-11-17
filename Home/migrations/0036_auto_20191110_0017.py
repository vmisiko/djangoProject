# Generated by Django 2.2.5 on 2019-11-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0035_auto_20191110_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('s', 'Bidding Account'), ('sw', 'Take Account'), ('OW', 'Transcribing Account')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
