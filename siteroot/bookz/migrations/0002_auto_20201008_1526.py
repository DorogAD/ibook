# Generated by Django 3.1.2 on 2020-10-08 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Город')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Статус предложения')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='town',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='books', to='bookz.town'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='books', to='bookz.type'),
            preserve_default=False,
        ),
    ]
