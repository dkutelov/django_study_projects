# Generated by Django 3.1.3 on 2020-11-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythons_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='python',
            name='python_image',
            field=models.ImageField(default='img.png', upload_to='images'),
            preserve_default=False,
        ),
    ]
