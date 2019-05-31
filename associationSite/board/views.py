from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Board, Comment
from .forms import BoardForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class BoardList(generic.ListView):
    model = Board
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'

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
        messages.info(request, 'You are not allowed')
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