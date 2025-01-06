# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment, Profile
from .forms import PostForm, CategoryForm, ProfileForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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

@login_required
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

def recursos(request):
    return render(request, 'blog/recursos.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login tras el registro
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    # Crear el perfil automáticamente si no existe
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    return render(request, 'blog/profile.html', {'user': request.user})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent__isnull=True)  # Obtener solo comentarios principales

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Asegúrate de que el usuario esté autenticado
            comment.save()
            return redirect('post_detail', slug=post.slug)  # Redirige para limpiar el formulario
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})