# Generated by Django 2.2.6 on 2021-02-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgtext', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgfile',
            name='text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]