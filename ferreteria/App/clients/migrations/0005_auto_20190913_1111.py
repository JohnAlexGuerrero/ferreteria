# Generated by Django 2.2.4 on 2019-09-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
        ('clients', '0004_facturaclient_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaclient',
            name='producto',
        ),
        migrations.AddField(
            model_name='facturaclient',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto'),
        ),
        migrations.CreateModel(
            name='pedidoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
            ],
        ),
    ]
