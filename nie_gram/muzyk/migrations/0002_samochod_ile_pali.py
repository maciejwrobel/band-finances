# Generated by Django 3.1 on 2020-09-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzyk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='ile_pali',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=4),
            preserve_default=False,
        ),
    ]
