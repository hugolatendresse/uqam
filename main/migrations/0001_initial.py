# Generated by Django 3.1.1 on 2021-06-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atext', models.CharField(max_length=1024)),
                ('qnumber', models.IntegerField()),
                ('anumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtext', models.CharField(max_length=1024)),
                ('qnumber', models.IntegerField()),
            ],
        ),
    ]
