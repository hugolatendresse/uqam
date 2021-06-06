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
                ('anumber', models.CharField(max_length=1024)),
                ('q_to_skip', models.CharField(default='', editable=False, max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Conseil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctext', models.CharField(max_length=1024)),
                ('q1', models.CharField(default='<any>', editable=False, max_length=1024)),
                ('q2', models.CharField(default='<any>', editable=False, max_length=1024)),
                ('q3', models.CharField(default='<any>', editable=False, max_length=1024)),
                ('q4', models.CharField(default='<any>', editable=False, max_length=1024)),
                ('q5', models.CharField(default='<any>', editable=False, max_length=1024)),
                ('q6', models.CharField(default='<any>', editable=False, max_length=1024)),
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
        migrations.CreateModel(
            name='RandomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(default='Ask', editable=False, max_length=1024)),
                ('q2', models.CharField(default='Ask', editable=False, max_length=1024)),
                ('q3', models.CharField(default='Ask', editable=False, max_length=1024)),
                ('q4', models.CharField(default='Ask', editable=False, max_length=1024)),
                ('q5', models.CharField(default='Ask', editable=False, max_length=1024)),
                ('q6', models.CharField(default='Ask', editable=False, max_length=1024)),
            ],
        ),
    ]
