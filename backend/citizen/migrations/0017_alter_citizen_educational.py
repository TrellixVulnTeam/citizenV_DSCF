# Generated by Django 3.2.2 on 2021-12-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0016_auto_20211206_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='educational',
            field=models.CharField(choices=[('none', 'None'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('high', 'High'), ('university', 'University'), ('master', 'Master')], default='high', max_length=30),
        ),
    ]
