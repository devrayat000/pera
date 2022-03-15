# Generated by Django 4.0.3 on 2022-03-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_class_tests_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='subject',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='class_tests',
            name='subject',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='class_tests',
            name='type',
            field=models.CharField(choices=[('mcq', 'Mcq'), ('written', 'Written')], default='mcq', max_length=10),
        ),
    ]
