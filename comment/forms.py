from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control   ',
        'placeholder': "Write some nice stuff or nothing...",
        'cols': '40',
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ['content']
