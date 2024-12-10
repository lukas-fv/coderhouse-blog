from django import forms
from .models import Category, Post, User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)