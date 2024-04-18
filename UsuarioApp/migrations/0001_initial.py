# Generated by Django 4.2.11 on 2024-04-18 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ala', models.CharField(choices=[('Ala 1', 'Ala 1'), ('Ala 2', 'Ala 2'), ('Ala 3', 'Ala 3'), ('Ala 4', 'Ala 4')], max_length=10, verbose_name='Ala')),
                ('quarto', models.IntegerField(max_length=1, verbose_name='Quarto')),
                ('lider', models.BooleanField(default=False, verbose_name='Lider de ala')),
                ('em_dia_limpeza', models.BooleanField(default=False, verbose_name='Em dia com a Limpeza')),
                ('em_dia_taxa', models.BooleanField(default=False, verbose_name='Em dia com a Taxa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
