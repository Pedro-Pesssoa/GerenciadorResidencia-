# Generated by Django 4.2.11 on 2024-04-18 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TaxaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcompanhamentoTaxa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprovante', models.FileField(upload_to='', verbose_name='Comprovante')),
                ('comentario', models.TextField(max_length=1000, verbose_name='comentario')),
                ('taxa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaxaApp.taxa', verbose_name='Taxa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Acompanhamento da taxa',
                'verbose_name_plural': 'Acompanhamento das taxas',
            },
        ),
    ]
