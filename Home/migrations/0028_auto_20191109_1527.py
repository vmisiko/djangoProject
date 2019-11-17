# Generated by Django 2.2.5 on 2019-11-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0027_auto_20191028_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='diplay_pic',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='display_pics/%Y%m%d/'),
        ),
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
            model_name='lnmonline',
            name='Balance',
            field=models.CharField(default=0, max_length=12),
        ),
    ]
