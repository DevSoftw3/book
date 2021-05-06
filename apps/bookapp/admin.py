from django.contrib import admin

from apps.bookapp.models import BookModel, CategoryModel, BookSearchModel


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(CategoryModel,CategoryAdmin)
admin.site.register(BookModel,BookAdmin)


admin.site.register(BookSearchModel)

