# Generated by Django 4.1.3 on 2022-11-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportlockerShop', '0004_ropa_articulotop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='imagen',
            field=models.TextField(),
        ),
    ]
