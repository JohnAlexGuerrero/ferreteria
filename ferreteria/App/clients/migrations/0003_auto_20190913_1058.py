# Generated by Django 2.2.4 on 2019-09-13 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20190913_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='typePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtp', models.IntegerField(default=20)),
                ('nomtypepago', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idclie',
            field=models.IntegerField(default=10),
        ),
        migrations.CreateModel(
            name='facturaClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.IntegerField()),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Cliente')),
                ('formaPago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.typePago')),
            ],
        ),
    ]