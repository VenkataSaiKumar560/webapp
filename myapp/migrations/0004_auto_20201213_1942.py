# Generated by Django 3.1.1 on 2020-12-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201213_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FID', models.CharField(max_length=30, unique=True)),
                ('FName', models.CharField(max_length=40)),
                ('FEmail', models.EmailField(max_length=254, null=True, unique=True)),
                ('FPhone', models.CharField(max_length=10)),
                ('FPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='Email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
