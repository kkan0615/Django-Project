from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Post, Community
from .forms import CommunityCreateForm

class CommunityList(generic.ListView):
    model = Community
    template_name = 'community/community_list.html'
    context_object_name = 'community_list'

    def get_queryset(self):
        order = self.request.GET.get('order', 'title')
        return Community.objects.order_by(order)

class CommunityDetail(generic.ListView):
    model = Community
    template_name = 'community/community_detail.html'
    context_object_name = 'community'

class LatestView(generic.ListView):
    model = Post
    template_name = 'post/post_latest_list.html'
    paginate_by = 20

    def get_queryset(self):
        order = self.request.GET.get('order', '-created_date')
        return Post.objects.order_by(order)

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

def editCommunity(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if community.manager != request.user:

        return redirect('community:community_detail', url_key=community.url_key)

    if request.method == 'POST':
        form = CommunityCreateForm(request.POST, instance=community)