# Generated by Django 3.0.6 on 2020-05-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='default.png', upload_to='stuff'),
        ),
    ]