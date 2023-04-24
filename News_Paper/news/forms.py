from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Post_News


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_header',
            'post_body',
            'author',
            'category',

       ]

class PostFormNews(forms.ModelForm):
    class Meta:
        model = Post_News
        fields = [
            'post_header',
            'post_body',
            'author',
            'category',


        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get("description")
    #     if description is not None and len(description) < 20:
    #         raise ValidationError({
    #             "description": "Описание не может быть менее 20 символов."
    #         })
    #
    #     return cleaned_data