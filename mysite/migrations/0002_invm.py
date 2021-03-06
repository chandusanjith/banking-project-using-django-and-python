# Generated by Django 3.0.2 on 2020-04-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='invm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginid', models.CharField(max_length=16)),
                ('custnum', models.CharField(max_length=16)),
                ('acctype', models.CharField(max_length=2)),
                ('opendate', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=2)),
                ('curency', models.CharField(max_length=3)),
                ('balance', models.CharField(max_length=17)),
                ('accname', models.CharField(max_length=50)),
                ('intrest', models.CharField(max_length=3)),
                ('intfreq', models.CharField(max_length=5)),
                ('matdate', models.CharField(max_length=15)),
                ('narration', models.CharField(max_length=50)),
            ],
        ),
    ]
