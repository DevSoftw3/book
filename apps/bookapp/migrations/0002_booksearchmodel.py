# Generated by Django 3.1.5 on 2021-03-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100, verbose_name='Nombre del Libro')),
            ],
            options={
                'verbose_name': 'Book-Search',
                'verbose_name_plural': 'Book-Searchs',
                'ordering': ['id'],
            },
        ),
    ]
