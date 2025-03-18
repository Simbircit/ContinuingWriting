from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.db.models import Count


def main(request):

    posts = Post.objects.order_by('-changed', '-published', 'title')
    posts_best = Post.objects.order_by('likes')[0:5]

    return render(request, 'main.html', {'posts': posts, 'posts_best': posts_best})


def profile(request):

    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect(f'/create_profile/{username}', {form.cleaned_data['username']})
    else:
        form = UserCreationForm

    return render(request, 'register.html', {'form': form})


def create_profile(request, username):
    profile_obj = Profile()
    profile_obj.user = User.objects.get(username=username)
    profile_obj.save()

    return redirect('/')


def logout_url(request):
    logout(request)
    return redirect('/')


def post_page(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    continues = PostContinue.objects.filter(post__id=post_id)
    comments = Comment.objects.filter(post__id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = Comment()
        comment.author = User.objects.get(username=request.user.username)
        comment.post = Post.objects.get(id=post_id)
        comment.text = request.POST.get('text')
        comment.save()
    else:
        form = CommentForm()
    context = {'post': post, 'continues': continues, 'comments': comments, 'form': form}
    return render(request, 'post.html', context)


def post_continue(request, continue_id):

    post = get_object_or_404(PostContinue, id=continue_id)
    comments = Comment.objects.filter(postcontiue__id=continue_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = Comment()
        comment.author = User.objects.get(username=request.user.username)
        comment.post = Post.objects.get(id=continue_id)
        comment.text = request.POST.get('text')
        comment.save()
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'post_continue.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        post = Post()
        post.save()
    else:
        form = PostCreateForm(request.POST)
    render(request, 'post_create.html', {'form': form})


def continue_create(request):
    if request.method == 'POST':
        form = ContinueCreationForm(request.POST, request.FILES)
        post = PostContinue()
        post.save()
    else:
        form = PostCreateForm(request.POST)
    render(request, 'post_create.html', {'form': form})
