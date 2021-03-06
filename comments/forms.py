from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'qq', 'wechat', 'url', 'text']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'qq': TextInput(attrs={'class': 'form-control'}),
            'wechat': TextInput(attrs={'class': 'form-control'}),
            'url': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
