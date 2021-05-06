from django.views import View

from apps.bookapp.form import BookSearchForm
from apps.bookapp.models import CategoryModel


def category_links(request):
    category = CategoryModel.objects.all()
    return {'categories':category}


def boo_forms(request):
    search_form = BookSearchForm()
    if request.method=='POST':
        search_form = BookSearchForm(request.POST)
        if search_form.is_valid():
            search_form.save()
    return {'search_form':search_form}