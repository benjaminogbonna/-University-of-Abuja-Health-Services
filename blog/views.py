from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from .models import Post
from .forms import PostForm


def post_list(request):
    all_post = Post.objects.all().order_by('-created_at')
    latest_posts = Post.objects.all().order_by('-created_at')[:3]

    paginator = Paginator(all_post, 4)  # show 3 posts on each page
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    context = {
        'post': post,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/post_detail.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def add_post(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.save()
                messages.success(request, 'post published successfully!')
                return redirect('blog:author_post_list')
            else:
                messages.error(request, "An error occurred, please try again!")
        else:
            form = PostForm()

        context = {
            'form': form,
        }
        return render(request, 'blog/add_post.html', context)
    else:
        return redirect('main:index')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def author_post_list(request):
    user = request.user
    if request.user.is_staff:
        all_post = user.posts.all().order_by('-created_at')
        post_count = user.posts.all()
        latest_posts = user.posts.all().order_by('-created_at')[:3]
        paginator = Paginator(all_post, 4)  # show 3 posts on each page
        page = request.GET.get('page', 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            posts = paginator.page(1)
        except EmptyPage:
            # if page is out of range, deliver last page of results
            posts = paginator.page(paginator.num_pages)
        context = {
            'page': page,
            'posts': posts,
            'post_count': post_count,
            'latest_posts': latest_posts,
        }
        return render(request, 'blog/author_post_list.html', context)
    else:
        return redirect('main:index')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def edit_post(request, slug, id):
    post = get_object_or_404(Post, slug=slug, id=id)
    if request.user.is_staff:
        if request.user == post.author:
            if request.method == 'POST':
                form = PostForm(instance=post, data=request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.slug = slugify(post.title)
                    post.save()
                    messages.success(request, 'post updated successfully!')
                    return redirect('blog:author_post_list')
            else:
                form = PostForm(instance=post)
        else:
            return redirect('doctor:profile')
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'blog/edit_post.html', context=context)
    else:
        return redirect('main:index')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def delete_post(request, slug, id):
    post = get_object_or_404(Post, slug=slug, id=id)
    if request.user.is_staff:
        if request.user == post.author:
            context = {
                'post': post,
            }
            return render(request, 'blog/delete_post.html', context)
        else:
            return redirect('blog:author_post_list')
    else:
        return redirect('main:index')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def confirm_delete_post(request, slug, id):
    post = get_object_or_404(Post, slug=slug, id=id)
    if request.user.is_staff:
        if request.user == post.author:
            post.delete()
            messages.success(request, 'Post deleted successfully!')
            return redirect('blog:author_post_list')
        else:
            return redirect('blog:author_post_list')
    else:
        return redirect('main:index')
