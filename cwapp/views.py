from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def main(request):

    posts = Post.objects.order_by('-changed', '-published', 'title')
    posts_best = Post.objects.order_by('likes')[0:5]

    return render(request, 'main.html', {'posts': posts, 'posts_best': posts_best})


def profile(request):

    posts = Post.objects.filter(author=request.user.id)
    if request.method == 'POST':
        avatar_form = ProfileAvatarUpdate(request.POST, request.FILES, instance=request.user.profile)
        profile_form = ProfileEdit(request.POST, request.FILES, instance=request.user)
        if avatar_form.is_valid():
            avatar_form.save()
        if profile_form.is_valid():
            user_edit = request.user
            user_edit.username = request.POST.get('username')
            user_edit.first_name = request.POST.get('first_name')
            user_edit.email = request.POST.get('email')
            user_edit.save()

        return redirect('profile')
    else:
        avatar_form = ProfileAvatarUpdate(instance=request.user.profile)
        profile_form = ProfileEdit(instance=request.user)

    context = {'avatar_form': avatar_form, 'profile_form': profile_form, 'posts': posts}

    return render(request, 'profile.html', context)


def another_profile(request, username):

    user = User.objects.get(username=username)
    profile_obj = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=user.id)

    context = {'posts': posts, 'profile_obj': profile_obj}

    return render(request, 'another_profile.html', context)


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

    post_continue = get_object_or_404(PostContinue, id=continue_id)
    comments = Comment.objects.filter(post_continue_id=continue_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = Comment()
        comment.author = User.objects.get(username=request.user.username)
        comment.post_continue = PostContinue.objects.get(id=continue_id)
        comment.text = request.POST.get('text')
        comment.save()
    else:
        form = CommentForm()

    context = {'post_continue': post_continue, 'comments': comments, 'form': form}
    return render(request, 'post_continue.html', context)


def post_info(request, post_id):

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

    return render(request, 'post_info.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        post = Post()
        post.author = User.objects.get(username=request.user.username)
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.start_title = request.POST.get('start_title')
        post.post_start = request.POST.get('post_start')
        post.end_title = request.POST.get('end_title')
        post.post_end = request.POST.get('post_end')
        post.status = request.POST.get('status')
        post.image = request.FILES.get('image')
        post.continues_max = request.POST.get('continues_max')
        post.save()

        return redirect('/')
    else:

        form = PostCreateForm(request.POST)
    return render(request, 'post_create.html', {'form': form})


def continue_create(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    post_chapter = post.continues_count + 1

    if request.method == 'POST':
        form = ContinueCreationForm(request.POST, request.FILES)
        post_continue = PostContinue()
        post_continue.post = get_object_or_404(Post, id=post_id)
        post_continue.chapter = post_chapter
        post_continue.author = User.objects.get(username=request.user.username)
        post_continue.title = request.POST.get('title')
        post_continue.text = request.POST.get('text')
        post_continue.image = request.FILES.get('image')
        post_continue.save()
        post.continues_count += 1
        post.save()

        return redirect('/')
    else:
        form = ContinueCreationForm(request.POST)
    return render(request, 'post_create.html', {'form': form})


@login_required
def like_post(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    if request.user in post_obj.likes.all():
        post_obj.likes.remove(request.user)
    else:
        post_obj.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))


def post_delete(request, post_id):

    post_obj = Post.objects.get(id=post_id)
    post_obj.delete()
    return redirect(request.META.get('HTTP_REFERER'))
