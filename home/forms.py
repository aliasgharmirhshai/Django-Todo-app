from curses.ascii import LF
from venv import create
from django import forms
from .models import Todo
# Create your forms here.

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()
     
#Update Todo Task
class TodoUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Todo
       #fields = ("title", "body", "created")
        fields = ('__all__')



    
