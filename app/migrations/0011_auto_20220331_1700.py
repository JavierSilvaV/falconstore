# Generated by Django 3.2.4 on 2022-03-31 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220331_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marcas',
            old_name='marca',
            new_name='img',
        ),
        migrations.AddField(
            model_name='marcas',
            name='nombre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
