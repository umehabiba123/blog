# Generated by Django 5.0.3 on 2024-03-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]