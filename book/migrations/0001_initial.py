# Generated by Django 3.2.6 on 2021-08-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('is_publish', models.BooleanField(default=False)),
                ('publish_date', models.DateField(null=True)),
                ('is_deleted', models.CharField(default=0, max_length=1)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
