# Generated by Django 3.1.7 on 2023-10-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('imgUrl', models.ImageField(upload_to='')),
                ('categoryId', models.CharField(max_length=20)),
            ],
        ),
    ]
