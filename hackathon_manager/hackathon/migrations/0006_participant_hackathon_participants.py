# Generated by Django 4.2 on 2023-05-07 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0005_alter_hackathon_background_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='hackathon.hackathon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('hackathon', 'user')},
            },
        ),
        migrations.AddField(
            model_name='hackathon',
            name='participants',
            field=models.ManyToManyField(through='hackathon.Participant', to=settings.AUTH_USER_MODEL),
        ),
    ]
