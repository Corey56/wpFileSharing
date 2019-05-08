# Generated by Django 2.2 on 2019-05-07 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=5, unique=True)),
                ('class_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Academic_dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=10, unique=True)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=30, unique=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.Academic_class')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
        migrations.AddField(
            model_name='academic_class',
            name='dept_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.Academic_dept'),
        ),
    ]
