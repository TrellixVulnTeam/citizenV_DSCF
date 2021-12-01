# Generated by Django 3.2.2 on 2021-12-01 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0001_initial'),
        ('citizen', '0004_citizen'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='citizens', to='agency.agency'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='educational',
            field=models.CharField(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('high', 'High'), ('university', 'University'), ('Master', 'Master')], default='high', max_length=30),
        ),
        migrations.AddField(
            model_name='citizen',
            name='marital_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='citizen',
            name='religion',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now=True)),
                ('declarer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declared_families', to=settings.AUTH_USER_MODEL)),
                ('head', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='own_family', to='citizen.citizen')),
            ],
        ),
    ]
