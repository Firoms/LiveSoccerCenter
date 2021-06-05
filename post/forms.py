from django import forms
from django.forms.widgets import ClearableFileInput, FileInput
from .models import Post

# class AddForm(forms.Form):
#     title = forms.CharField(label="제목", max_length=30)
#     content = forms.CharField(label="내용")
#     files = forms.FileField(label="파일")


class AddForm(forms.ModelForm):
    # files = forms.FileField(label="File", widget=ClearableFileInput)
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'files'
        ]
        # label 키워드
