# Generated by Django 4.2 on 2023-05-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_alter_hackathon_background_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='background_image',
            field=models.ImageField(upload_to='media/background_image/'),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_image',
            field=models.ImageField(upload_to='media/hackathon_image/'),
        ),
    ]
