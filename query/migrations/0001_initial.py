# Generated by Django 2.2.5 on 2020-07-15 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('result_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Users')),
                ('hashtag', models.ManyToManyField(to='query.Hashtags')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Queries')),
            ],
        ),
        migrations.CreateModel(
            name='Mentions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Results')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Users')),
            ],
        ),
    ]