from django.shortcuts import render
from django.views import generic
from .models import Board, Comment
from .forms import BoardForm

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

def board_new(request):
    form = BoardForm()
    return render(request, 'board/board_edit.html') # board edit create