from django import forms
from .models import CodeSnippet, Tag

class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = [
            'title',
            'body',
            'language',
            'is_public',
        ]