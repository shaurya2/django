# Generated by Django 4.0.4 on 2022-05-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(max_length=500),
        ),
    ]
