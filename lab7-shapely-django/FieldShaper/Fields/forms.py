from django.forms import ModelForm
from django import forms
from .models import Field

class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = '__all__' #['field_name'] # or '__all__' to display all fields

class FieldSelect(ModelForm):
  fields = forms.ChoiceField(choices=[(field.id, field.field_name) for field in Field.objects.all()])
  class Meta:
      model = Field
      fields = ('fields',)
      widgets = {
          'fields': forms.Select(attrs={'class': 'select'}),
      }