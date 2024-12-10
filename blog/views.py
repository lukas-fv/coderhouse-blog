# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, User
from .forms import PostForm, CategoryForm, UserForm, SearchForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'blog/add_category.html', {'form': form})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})