# Generated by Django 4.0.4 on 2022-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.istockphoto.com/photo/straight-down-above-tall-towers-rising-over-austin-texas-gm1320415956-406986223?utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_top&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fview&utm_term=view%3A%3Asearch-explore-top-affiliate-outside-feed-x-v2%3Ab', max_length=500),
        ),
    ]
