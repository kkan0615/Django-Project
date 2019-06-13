from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Board, Comment # Models (DB)
from .forms import BoardForm # Board form
from django.utils import timezone # For current time
from django.contrib import messages # https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse # For HttpResponse https://docs.djangoproject.com/en/2.2/ref/request-response/
from django.http import JsonResponse
import json # Json foramt
from hitcount.views import HitCountDetailView

# If it's not class view https://cjh5414.github.io/django-pagination/
# Pagination https://docs.djangoproject.com/en/1.10/topics/pagination/
class BoardList(generic.ListView):
    model = Board
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'
    paginate_by = 5

    def get_queryset(self):
        order = self.request.GET.get('order', '-created_date')
        return Board.objects.order_by(order)


class BoardList_order_date(generic.ListView):
    model = Board
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'
    paginate_by = 5

    def get_queryset(self):
        return Board.objects.order_by('-created_date')

class CommentList(generic.ListView):
    model = Comment

class BoardDetail(HitCountDetailView):
    model = Board
    count_hit = True
    template_name = 'board/board_detail.html'
    context_object_name = 'board'

class CommnetDetail(generic.DetailView):
    model = Comment

# Create new post
def board_new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.author = request.user
            board.created_date = timezone.now()
            board.save()
            return redirect('board:board_detail', pk = board.pk)
    else:
        form = BoardForm()

    return render(request, 'board/board_edit.html', {'form': form})

# Edit post
@login_required
def board_edit(request, pk):
    board = get_object_or_404(Board, pk = pk)
    if board.author != request.user:
        messages.error(request, 'Permission denided, You are not permitted to edit this post')
        return redirect('board:board_detail', pk = board.pk)

    if request.method == 'POST':
        form = BoardForm(request.POST, instance = board)
        if form.is_valid():
            board = form.save(commit=False)
            board.created_date = timezone.now()
            board.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm(instance = board)
    return render(request, 'board/board_edit.html', {'form': form})

@login_required
def comment_new(request, board_pk):
    if request.method == 'POST':
        board = get_object_or_404(Board, pk = board_pk)
        content = request.POST.get('content')

        if not content:
            messages.error(request, 'You did not write anything')
            return redirect('board:board_detail', pk = board.pk)

        comment = Comment(author = request.user, post = board, content = content, created_date = timezone.now())
        comment.save()
        return redirect('board:board_detail', pk = board.pk)

@login_required
def board_remove(request, pk):
    board = get_object_or_404(Board, pk = pk)
    if board.author == request.user:
        board.delete()
        return redirect('board:board_list', page = 0)

    else:
        messages.error(request, 'You do not have permission to delete this post')

    return redirect('board:board_detail', pk = board.pk)

def comment_remove(request):
    if request.method == 'POST':
        comment_pk = request.POST.get('comment_pk')
        comment = get_object_or_404(Comment, pk = comment_pk)


        if comment.author != request.user:
            message = 'You are not allowed to delete this comment'

        else:
            comment.delete()
            message = 'Comment Deleted'

        response_data = {
            'message' : message
        }

        JsonResponse(response_data)
    #return HttpResponse(json.dumps(response_data), content_type="application/json")