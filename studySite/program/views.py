from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Code, Program, Subject, Subject_comment, Chapter
from account.models import User
from .forms import ProgramCreateForm, SubjectForm, ChapterForm

def programList(request):
    if request.method == 'GET':
        code = request.GET.get('code', None)
        if code:
            programs = Program.objects.all().filter(codes__name=code)
        else:
            programs = Program.objects.all()
        order = request.GET.get('order', '-created_date')
        programs.order_by(order)
        codes = Code.objects.all().order_by('-name')
        return render(request, 'program/program_list.html', {'programs': programs, 'codes': codes})

@login_required
def create_program(request):
    if request.method == 'POST':
        form = ProgramCreateForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.author = request.user
            program.save()
            return redirect('program:program_detail', url_key=program.url_key)
        else:
            messages.error(request, 'invalid form!')
            return render(request, 'program/create_program.html', { 'form': form  })
    else:
        form = ProgramCreateForm()

    return render(request, 'program/create_program.html', { 'form': form  })

def program_detail(request, url_key):
    if request.method == 'GET':
        program = get_object_or_404(Program, url_key=url_key)
        order = request.GET.get('order', '-created_date')
        subjects = Subject.objects.all().order_by(order)
        chapters = Chapter.objects.all()
        return render(request, 'program/program_detail.html', { 'program': program, 'chapters': chapters, 'subjects': subjects })

def create_chapter(request, url_key):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            program = get_object_or_404(Program, url_key=url_key)
            chapter = form.save(commit=False)
            chapter.program = program
            chapter.save()
            return redirect('program:program_detail', url_key=chapter.program.url_key)
        else:
            return render(request, 'program/create_chapter.html', { 'form': form  })
    else:
        form = ChapterForm()
    return render(request, 'program/create_chapter.html', { 'form': form  })

def create_subject(request, url_key, pk):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            program = get_object_or_404(Program, url_key=url_key)
            chapter = get_object_or_404(Chapter, pk=pk)
            subject = form.save(commit=False)
            subject.program = program
            subject.chapter = chapter
            subject.edit_date = timezone.now()
            subject.save()
            return redirect('program:program_detail', url_key=subject.program.url_key)
        else:
            messages.error(request, 'invalid error')
            return render(request, 'program/subject_create.html', { 'form': form  })
    else:
        form = SubjectForm()
    return render(request, 'program/subject_create.html', { 'form': form  })
