# Generated by Django 3.1.5 on 2021-03-04 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.singermodel')),
            ],
        ),
    ]
