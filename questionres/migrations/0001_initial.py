# Generated by Django 2.1 on 2019-04-02 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('isMcq', models.BooleanField(blank=True, default=True)),
                ('options', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('resid', models.AutoField(primary_key=True, serialize=False)),
                ('response', models.CharField(max_length=50)),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionres.Questions')),
            ],
            options={
                'db_table': 'responses',
            },
        ),
    ]
