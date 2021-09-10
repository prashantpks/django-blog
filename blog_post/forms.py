from django import forms
from .models import Comment, Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)