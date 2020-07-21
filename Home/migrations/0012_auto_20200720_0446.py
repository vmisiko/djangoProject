# Generated by Django 2.2.5 on 2020-07-20 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20200720_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Level',
            field=models.CharField(blank=True, choices=[('Juniour', 'Junior'), ('Ivy', 'Ivy'), ('Senior', 'Senior'), ('Intermediate', 'Intermediate')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=1),
        ),
    ]