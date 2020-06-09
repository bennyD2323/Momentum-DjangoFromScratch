from django import forms
from .models import CodeSnippet, Tag

class CodeSnippetForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput)
    class Meta:
        model = CodeSnippet
        fields = [
            'title',
            'body',
            'language',
            'is_public',
        ]
        # widgets = {
        #     'title': forms.TextInput,
        #     'body': forms.TextInput,
        #     'language': forms.TextInput,
        #     'is_public': forms.BooleanField
        # }