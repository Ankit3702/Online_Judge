# Generated by Django 4.0.5 on 2024-01-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_OJ', '0011_remove_test_cases_id_test_cases_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_cases',
            name='p_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
