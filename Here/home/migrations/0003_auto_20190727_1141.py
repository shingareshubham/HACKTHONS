# Generated by Django 2.2.3 on 2019-07-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register_case_reasone'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_case',
            name='lat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register_case',
            name='long',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register_case',
            name='mobile_no',
            field=models.CharField(max_length=50),
        ),
    ]