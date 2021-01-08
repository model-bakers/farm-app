# Generated by Django 3.1.3 on 2021-01-08 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('area', models.DecimalField(decimal_places=16, max_digits=22)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('farm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField()),
                ('specie', models.CharField(choices=[('COW', 'cow'), ('DUC', 'duck'), ('HOR', 'horse'), ('CHI', 'chicken'), ('NAN', 'not_identified_yet')], max_length=3)),
                ('farm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.farm')),
            ],
        ),
    ]