# Generated by Django 4.0.4 on 2022-05-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fplaceholder-restaurant&psig=AOvVaw0XnCxQPPanY1mrCUTBVHbs&ust=1651936626935000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKik49CVy_cCFQAAAAAdAAAAABAa', max_length=500),
        ),
    ]
