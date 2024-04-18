# Generated by Django 4.2.11 on 2024-04-16 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('data', models.DateField()),
            ],
            options={
                'verbose_name': 'Taxa',
                'verbose_name_plural': 'Taxas',
            },
        ),
    ]