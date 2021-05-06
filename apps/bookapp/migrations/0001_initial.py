# Generated by Django 3.1.5 on 2021-03-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('slug', models.SlugField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='img', verbose_name='Imagen')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('summary', models.TextField(verbose_name='Resumen')),
                ('pdf', models.FileField(upload_to='pdf')),
                ('backend_books', models.BooleanField(default=False, verbose_name='Libros de BackEnd')),
                ('frontend_books', models.BooleanField(default=False, verbose_name='Libros de FrontEnd')),
                ('datascience_books', models.BooleanField(default=False, verbose_name='Libros de Ciencia de Datos')),
                ('category', models.ManyToManyField(related_name='books', to='bookapp.CategoryModel')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['id'],
            },
        ),
    ]