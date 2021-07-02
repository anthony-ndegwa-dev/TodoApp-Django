from django import forms
from todo.models import Todoing

class TodoingForm(forms.ModelForm):
    class Meta:
        model = Todoing
        fields = ['subject', 'task']

class RawTodoForm(forms.Form):
    subject     =   forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Subject", "class": "baron", "size": 80}))
    task        =   forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder": "Task", "class": "boron", "id": "textarea", "contenteditable": "true"}))
    date     =   forms.DateField(label='', widget=forms.DateInput(attrs={"type": "date", "class": "fin"}))
