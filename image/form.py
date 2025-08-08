from django import forms
from .models import Image

class Imageform(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['caption','image','experience']

caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
experience= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review'}))
image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))