from django.shortcuts import render, redirect, HttpResponse
from .forms import DefaultForm
from .models import DefaultFormData, EditedFormData

def single_page_form(request):
    form = DefaultForm()
    if request.method == 'POST':
        if 'submit_default_form' in request.POST:
            form = DefaultForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("Default form has been submitted!")
        elif 'submit_edited_form' in request.POST:
            edited_form_data = []
            for key, value in request.POST.items():
                if key.startswith('field_name_') and value:
                    field_name = value
                    field_value = request.POST.get('field_value_' + key.split('_')[-1], '')
                    edited_form_data.append(EditedFormData(field_name=field_name, field_value=field_value))
            EditedFormData.objects.bulk_create(edited_form_data)
            return HttpResponse("Edited form has been submitted!")
    return render(request, 'single_page_form.html', {'form': form})
