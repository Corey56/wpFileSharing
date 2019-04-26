# Generated by Django 2.2 on 2019-04-26 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wpFiles', '0009_auto_20190425_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upload',
            options={'ordering': ['-upload_date', '-flags']},
        ),
        migrations.RemoveField(
            model_name='upload',
            name='downloads',
        ),
        migrations.AlterField(
            model_name='academic_class',
            name='dept_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.Academic_dept'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='class_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.Academic_class'),
        ),
    ]
