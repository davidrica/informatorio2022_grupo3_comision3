# Generated by Django 4.0.8 on 2022-12-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_alter_noticias_categoria_alter_noticias_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='bajada',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=10),
        ),
    ]