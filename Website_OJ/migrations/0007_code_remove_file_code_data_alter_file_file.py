# Generated by Django 4.0.5 on 2022-08-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_OJ', '0006_file_code_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_data', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='code_data',
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]