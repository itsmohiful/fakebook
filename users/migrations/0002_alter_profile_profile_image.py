# Generated by Django 4.0.3 on 2022-03-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile_picture/defuault.jpg', upload_to='profile_picture'),
        ),
    ]
