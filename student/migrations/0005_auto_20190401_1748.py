# Generated by Django 2.1.7 on 2019-04-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20180703_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='t_age',
            field=models.IntegerField(max_length=21),
        ),
    ]