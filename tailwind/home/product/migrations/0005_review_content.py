# Generated by Django 4.2.2 on 2023-06-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_options_alter_product_options_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
