from django.db import models



class CategoryModel(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100, null=False, unique=True )
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class BookModel(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to='img', verbose_name='Imagen')
    author = models.CharField(max_length=100, verbose_name='Autor')
    summary = models.TextField(verbose_name='Resumen')
    category = models.ManyToManyField(CategoryModel, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    backend_books = models.BooleanField(default=False, verbose_name='Libros de BackEnd')
    frontend_books = models.BooleanField(default=False, verbose_name='Libros de FrontEnd')
    datascience_books = models.BooleanField(default=False, verbose_name='Libros de Ciencia de Datos')
    Data_books = models.BooleanField(default=False, verbose_name='Libros de Bases de Datos')
    others_books = models.BooleanField(default=False, verbose_name='Otros')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Book'
        verbose_name_plural = 'Books'
        ordering = ['id']


class BookSearchModel(models.Model):
    name_of_book = models.CharField(max_length=100, verbose_name='Nombre del Libro')

    def __str__(self):
        return self.name_of_book

    # class Meta:
    #     verbose_name='Book-Search'
    #     verbose_name_plural = 'Book-Searchs'
    #     ordering = ['id']