# Generated by Django 3.1.2 on 2020-10-21 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookz', '0002_auto_20201008_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['title'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='town',
            options={'ordering': ['title'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['title'], 'verbose_name': 'Вариант', 'verbose_name_plural': 'Варианты'},
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='bookz.category', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='books', to='bookz.Genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='book',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='bookz.town', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='bookz.type', verbose_name='Предложение'),
        ),
        migrations.AlterField(
            model_name='type',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Предложение'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='bookz.book', verbose_name='Владелец')),
            ],
        ),
    ]
