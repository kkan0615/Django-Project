from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from .models import Post, Community
from account.models import User
from .forms import CommunityCreateForm, PostForm

class CommunityList(generic.ListView):
    model = Community
    template_name = 'community/community_list.html'
    context_object_name = 'community_list'

    def get_queryset(self):
        order = self.request.GET.get('order', 'title')
        return Community.objects.order_by(order)

class LatestView(generic.ListView):
    model = Post
    template_name = 'post/post_latest_list.html'
    paginate_by = 20

    def get_queryset(self):
        order = self.request.GET.get('order', '-created_date')
        return Post.objects.order_by(order)

# https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
def CommunityDetail(request, url_key):
    if request.method == 'GET':
        community = get_object_or_404(Community, url_key=url_key)
        post_list = Post.objects.all().filter(community=community)
        manager = get_object_or_404(User, pk=community.manager.id)

        if not post_list:
            posts = None

        else:
            page = request.GET.get('page', 1)

            paginator = Paginator(post_list, 10)
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

        return render(request, 'community/community_detail.html', {
            'community': community,
            'posts': posts,
        })

def PostDetail(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        community = get_object_or_404(Community, pk=post.community.id)
        author = User.objects.filter(pk=post.author.id)
        manager = get_object_or_404(User, pk=community.manager.id)

        return render(request, 'post/post_detail.html', {
            'community': community,
            'post': post,
            'author': author,
            'manager': manager
        })

@login_required
def CreateNewCommunity(request):
    if request.method == 'POST':
        form = CommunityCreateForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.manager = request.user
            community.created_date = timezone.now()
            community.save()
            return redirect('community:community_detail', url_key=community.url_key)
        else:
            return render(request, 'community/community_create.html', { 'form': form  })

    else:
        form = CommunityCreateForm()

    return render(request, 'community/community_create.html', { 'form': form })

@login_required
def write_post(request, url_key):
    if request.method == 'POST':
        form = PostForm(request.POST)
        community = get_object_or_404(Community, url_key=url_key)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.community = community
            post.save()
            return redirect('post:post_detail', post.pk)
        else:
            return render(request, 'post/post_write.html', { 'form': form  })
    else:
        form = PostForm()

    return render(request, 'post/post_write.html', { 'form': form })
