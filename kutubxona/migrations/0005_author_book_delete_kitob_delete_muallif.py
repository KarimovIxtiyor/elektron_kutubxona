# Generated by Django 4.2.3 on 2023-09-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kutubxona', '0004_rename_kitobga_matn_kitob_kitob_matni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birth_year', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'auther',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, upload_to='images/')),
                ('body', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kutubxona.author')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.DeleteModel(
            name='Kitob',
        ),
        migrations.DeleteModel(
            name='Muallif',
        ),
    ]
