# Generated by Django 2.0.7 on 2019-05-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('volume', models.CharField(max_length=50)),
                ('versao', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
    ]