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
    posts = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def about_me(request):
    return render(request, "blog/about_me.html")

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})