# Generated by Django 2.1.7 on 2019-03-19 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osoby', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='absolwent',
            options={'verbose_name_plural': 'absolwenci'},
        ),
        migrations.AlterModelOptions(
            name='klasa',
            options={'ordering': ['rok_matury'], 'verbose_name_plural': 'klasy'},
        ),
    ]