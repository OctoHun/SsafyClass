from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
import random as random1

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid:
            issue = form.save()
            return redirect('eithers:detail', issue.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    commentform = CommentForm()
    comments = Comment.objects.all()
    count_red = 
    context = {
        'commentform': commentform,
        'comments': comments,
        'question': question,
    }
    return render(request, 'eithers/detail.html', context)


def random(request):
    question = random1.choice(Question.objects.all())
    return redirect('eithers:detail', question.pk)


def comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment = CommentForm(request.POST)
    new_comment = comment.save(commit=False)
    new_comment.question = question
    new_comment.save()
    return redirect('eithers:detail', question_pk)


def update(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid:
            issue = form.save()
            return redirect('eithers:detail', issue.pk)
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'eithers/update.html', context)


def delete_question(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    question.delete()
    return redirect('eithers:index')


def delete_comment(request, question_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('eithers:detail', question_pk)