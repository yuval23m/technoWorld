# Generated by Django 4.0.1 on 2022-05-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_marca_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='idpro',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
    ]
