# Generated by Django 4.2.3 on 2023-07-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
            ],
        ),
    ]