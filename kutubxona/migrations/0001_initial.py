# Generated by Django 4.2.3 on 2023-09-27 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('familya', models.CharField(max_length=50)),
                ('tugilgan_yil', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'muallif',
            },
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('janr', models.CharField(max_length=100)),
                ('rasm', models.ImageField(blank=True, upload_to='images/')),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kutubxona.muallif')),
            ],
            options={
                'db_table': 'kitoblar',
            },
        ),
    ]