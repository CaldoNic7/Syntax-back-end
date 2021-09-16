# Generated by Django 3.0 on 2021-09-16 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chars_per_min', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
                ('target_date', models.DateField()),
                ('practice_num', models.IntegerField()),
                ('measurement', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
