# Generated by Django 2.2.6 on 2021-02-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgtext', '0004_auto_20210222_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgfile',
            name='imgs',
            field=models.FileField(upload_to=''),
        ),
    ]