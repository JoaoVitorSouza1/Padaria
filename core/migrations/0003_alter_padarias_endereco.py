# Generated by Django 4.0.3 on 2022-03-31 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_endereço_padarias_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='padarias',
            name='endereco',
            field=models.CharField(max_length=100, verbose_name='Endereco'),
        ),
    ]
