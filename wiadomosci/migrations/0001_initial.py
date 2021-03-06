# Generated by Django 2.1.7 on 2019-03-19 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiadomosc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.TextField(verbose_name='wiadomość')),
                ('data_d', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dodana')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wiadomość',
                'verbose_name_plural': 'wiadomości',
            },
        ),
    ]
