# Generated by Django 2.2.5 on 2021-08-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20210811_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='b_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='BoardPhoto',
        ),
    ]