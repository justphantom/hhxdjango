from django import forms

# from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(label='名字', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    url = forms.URLField(label='网址', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    text = forms.CharField(label='评论', max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, }))
