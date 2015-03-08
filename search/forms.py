# -*- coding: utf-8 -*-
__author__ = 'Евгений'

from django import forms
from models import SearchTerm


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchTerm
        include = ('q',)
        widgets = {
            'q' : forms.TextInput(attrs={'class':'form-control', 'type':'text','placeholder':'Поиск по заголовкам...'})
        }
