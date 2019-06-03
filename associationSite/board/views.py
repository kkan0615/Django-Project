from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Board, Comment # Models (DB)
from .forms import BoardForm # Board form
from django.utils import timezone # For current time
from django.contrib import messages # https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse # For HttpResponse https://docs.djangoproject.com/en/2.2/ref/request-response/
import json # Json foramt

# If it's not class view https://cjh5414.github.io/django-pagination/
# Pagination https://docs.djangoproject.com/en/1.10/topics/pagination/
class BoardList(generic.ListView):
    model = Board
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'
    paginate_by = 5

class CommentList(generic.ListView):
    model = Comment

class BoardDetail(generic.DetailView):
    model = Board
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
        return redirect('board:board_list')

    else:
        messages.error(request, 'You do not have permission to delete this post')

    return redirect('board:board_detail', pk = board.pk)

def comment_remove(request, board_pk, comment_pk):
    board = get_object_or_404(Board, pk = board_pk)
    comment = get_object_or_404(Comment, pk = comment_pk)
    if comment.author != request.user:
        messages.error(request, 'You are not allowed to delete this comment')
        return redirect('board:board_detail', pk = board_pk)

    comment.delete()
    return redirect('board:board_detail', pk = board_pk)

# Through Ajax
# https://wayhome25.github.io/django/2017/06/25/django-ajax-like-button/
# https://stackoverflow.com/questions/1941212/correct-way-to-use-get-or-create
# -----------------IT'S NOT WORKING PLEASE FIX THIS--------------------------- #
@login_required
def board_like(request):
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        board = get_object_or_404(Board, pk=pk)
        likes, board_like_created = board.likes.get_or_create(author=request.user)

        if not board_like_created:
            likes.delete()
            message = 'Unlike'

        else:
            message = 'Like'

        context = {'like_count:': board.total_likes, 'message': message, 'nickname': request.user.nickname}
        #Json type
        return HttpResponse(json.dumps(context), content_type='application/json')