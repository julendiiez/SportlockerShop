# Generated by Django 4.1.3 on 2022-12-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportlockerShop', '0006_rename_contraseña_usuario_contrasenya'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa',
            old_name='imagen',
            new_name='imagen1',
        ),
        migrations.AddField(
            model_name='ropa',
            name='imagen2',
            field=models.TextField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ropa',
            name='imagen3',
            field=models.TextField(default=100),
            preserve_default=False,
        ),
    ]
