# Generated by Django 4.1.3 on 2022-11-19 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SportlockerShop', '0002_ropa_imagen_zapatilla_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ropa',
            name='talla',
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='id',
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='precio',
        ),
        migrations.AddField(
            model_name='zapatilla',
            name='ropa_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SportlockerShop.ropa'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('ropa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SportlockerShop.ropa')),
                ('talla', models.CharField(max_length=2)),
            ],
            bases=('SportlockerShop.ropa',),
        ),
        migrations.CreateModel(
            name='Sudadera',
            fields=[
                ('ropa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SportlockerShop.ropa')),
                ('conCapucha', models.BooleanField()),
                ('talla', models.CharField(max_length=2)),
            ],
            bases=('SportlockerShop.ropa',),
        ),
    ]