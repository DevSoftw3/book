from django.forms import *

from apps.bookapp.models import BookSearchModel, BookModel


class BookSearchForm(ModelForm):

    class Meta:
        model = BookSearchModel
        fields = ['name_of_book']

        widgets = {
            'name_of_book':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nombre del libro'
            })
        }


class RegisterForm(ModelForm):
    pdf = Field(widget=FileInput(attrs = {'id': 'upload-pdf','type': 'file', 'accept': '.pdf','style': 'display: none'}))
    cover_image = Field(widget=FileInput(attrs={'type':'file','accept':'image/jpeg, image/png','id':'upload-front-pdf','style':'display: none'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['backend_books'].widget.attrs['class']='form-check-input'
        self.fields['frontend_books'].widget.attrs['class']='form-check-input'
        self.fields['datascience_books'].widget.attrs['class']='form-check-input'
        self.fields['Data_books'].widget.attrs['class']='form-check-input'
        self.fields['others_books'].widget.attrs['class']='form-check-input'
        self.fields['title'].widget.attrs['placeholder']='Ejem: PHP, React, Python, Laravel'
        self.fields['author'].widget.attrs['placeholder']='Ejem: Mark Tielens Thomas'
        self.fields['summary'].widget.attrs['placeholder']='Una corta descripción del libro...'


    class Meta:
        model = BookModel
        fields = [
            'title',
            'cover_image',
            'author',
            'summary',
            'category',
            'pdf',
            'backend_books',
            'frontend_books',
            'datascience_books',
            'Data_books',
            'others_books',
        ]

        widgets = {
            'summary':Textarea(attrs={'rows':'3'}),
            'category':SelectMultiple(attrs=
                              {'id':'selectpicker',
                               'multiple':'true',
                               'title':'Selección Multiple',
                               'data-live-search':'true'
                               }),
            'backend_books':CheckboxInput(attrs={'id':'flexCheckDefault'}),
            'frontend_books':CheckboxInput(attrs={'id':'flexCheckChecked'}),
            'datascience_books':CheckboxInput(attrs={'id':'flexCheckCheckedes'}),
            'Data_books':CheckboxInput(attrs={'id':'flexCheckCheckedess'}),
            'others_books':CheckboxInput(attrs={'id':'flexCheckCheckedesss'}),
            'pdf': FileField(),
            'cover_image':ImageField(),
        }

    # <select id = "framework"  name = "frameworl" class ="form-control selectpicker" multiple >
