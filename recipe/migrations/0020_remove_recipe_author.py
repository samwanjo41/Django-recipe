# Generated by Django 3.0.8 on 2020-08-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0019_auto_20200819_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
    ]