# Generated by Django 3.2.23 on 2023-11-20 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_exercisecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userexercise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exerciseamount', to='main.exercisecategory')),
                ('userexercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exerciseamount', to='main.userexercise')),
            ],
        ),
    ]