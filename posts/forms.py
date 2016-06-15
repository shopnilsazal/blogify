from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "categories",
            "tags",
            "image"
        ]
