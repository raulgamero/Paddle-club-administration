# Generated by Django 4.2 on 2023-05-08 00:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('padel_admin', '0028_remove_cobramentsoci_soci_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugadors',
            fields=[
                ('id_jugador', models.CharField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('cognom', models.CharField(max_length=30)),
                ('nivell', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('telefon', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=50)),
                ('contrasenya', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pistes',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('tipus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('DNI', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('cognom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('contrasenya', models.CharField(max_length=30)),
                ('telefon', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Soci',
            fields=[
                ('jugadors_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='padel_admin.jugadors')),
                ('IBAN', models.CharField(max_length=34)),
            ],
            bases=('padel_admin.jugadors',),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horaInici', models.TimeField()),
                ('horaFinalitzacio', models.TimeField()),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padel_admin.jugadors')),
                ('pista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padel_admin.pistes')),
                ('recepcionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padel_admin.recepcionista')),
            ],
            options={
                'unique_together': {('jugador', 'data')},
            },
        ),
        migrations.CreateModel(
            name='Cobrament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=2)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padel_admin.jugadors')),
                ('recepcionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padel_admin.recepcionista')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padel_admin.reserva')),
            ],
        ),
        migrations.CreateModel(
            name='CobramentSoci',
            fields=[
                ('id_cobramentSoci', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('soci', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='padel_admin.soci')),
            ],
        ),
    ]
