from django import forms 
from .models import *
  
class imageForm(forms.ModelForm): 
  
    class Meta: 
        model = image
        fields = [ 'Img'] 