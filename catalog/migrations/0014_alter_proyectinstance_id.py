# Generated by Django 4.2.2 on 2023-07-07 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_proyectinstance_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectinstance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]