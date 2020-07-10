from django import forms

# from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    url = forms.URLField(label='Url', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    text = forms.CharField(label='Text', max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
