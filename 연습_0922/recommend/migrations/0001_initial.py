# Generated by Django 4.2.11 on 2024-09-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('report', models.TextField()),
                ('is_completed', models.BooleanField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('add_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
