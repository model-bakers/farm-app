# Generated by Django 3.1.3 on 2021-04-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0004_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='registration_document',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]