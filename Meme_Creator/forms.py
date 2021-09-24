from django import forms
from Home.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
