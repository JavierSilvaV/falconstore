# Generated by Django 3.2.4 on 2022-03-31 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_marcas_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='video',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
