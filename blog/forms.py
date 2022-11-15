from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """post form"""

    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'post title', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'post body', 'class': 'form-control'}),
        }
