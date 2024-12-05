# Generated by Django 5.1.1 on 2024-11-20 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LineInv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proyects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('areaKnowledge', models.CharField(max_length=100)),
                ('status', models.DateField(blank=True, null=True)),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('estatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
                ('typeStudent', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeProyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('doi', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=10)),
                ('magazine', models.CharField(max_length=100)),
                ('jcr', models.BooleanField(default=False)),
                ('impact', models.CharField(max_length=200)),
                ('datePublish', models.DateField(blank=True, null=True)),
                ('countryPublish', models.CharField(max_length=50)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=300)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area')),
            ],
        ),
        migrations.CreateModel(
            name='DetArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.articles')),
                ('workers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
        migrations.CreateModel(
            name='DetEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('workers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.events')),
            ],
        ),
        migrations.CreateModel(
            name='DetInvestigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('workers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lineinv')),
            ],
        ),
        migrations.CreateModel(
            name='DetProyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('workers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
                ('proyect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proyects')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.specialty')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='studies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.studies'),
        ),
        migrations.AddField(
            model_name='employee',
            name='studies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.studies'),
        ),
        migrations.AddField(
            model_name='events',
            name='typeEvent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typeevent'),
        ),
        migrations.AddField(
            model_name='proyects',
            name='typeProyect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typeproyect'),
        ),
        migrations.AddField(
            model_name='area',
            name='unities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.unities'),
        ),
    ]