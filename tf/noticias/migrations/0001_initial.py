# Generated by Django 4.0.8 on 2022-12-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('titulo', models.CharField(max_length=30)),
                ('bajada', models.CharField(max_length=30)),
                ('cuerpo', models.TextField()),
            ],
        ),
    ]