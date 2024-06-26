# Generated by Django 5.0.3 on 2024-04-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_organizer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapanevent',
            name='latitude',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='mapanevent',
            name='longitude',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
