# Generated by Django 4.2.11 on 2024-04-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LimpezaApp', '0003_alter_acompanhamentolimpeza_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='acompanhamentolimpeza',
            name='comodo',
            field=models.CharField(blank=True, choices=[('Sala computadores', 'computadores'), ('Sala estudos', 'Sala estudos'), ('Sala de baixo', 'Sala de baixo'), ('Sala de cima', 'Sala de cima'), ('Cozinha', 'Cozinha')], max_length=50, null=True, verbose_name='Ala'),
        ),
        migrations.AlterField(
            model_name='acompanhamentolimpeza',
            name='comentario',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='comentario'),
        ),
    ]