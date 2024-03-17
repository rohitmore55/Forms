from django.urls import path
from forms.views import single_page_form

urlpatterns = [
    path('single-page-form/', single_page_form, name='single_page_form'),
]
