# Generated by Django 3.0.8 on 2020-08-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20200818_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='recipe'),
        ),
    ]
