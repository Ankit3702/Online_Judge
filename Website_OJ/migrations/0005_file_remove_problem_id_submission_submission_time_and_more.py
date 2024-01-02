# Generated by Django 4.0.5 on 2022-08-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_OJ', '0004_problem_submission_test_cases'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='id',
        ),
        migrations.AddField(
            model_name='submission',
            name='submission_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]