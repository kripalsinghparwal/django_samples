from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm

# Register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login user
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout user
def user_logout(request):
    logout(request)
    return redirect('login')

# Home view with all questions
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})

# Post a new question
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

# View a question and its answers
def view_question(request, pk):
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('view_question', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'view_question.html', {'question': question, 'answers': answers, 'form': form})

# Like an answer
def like_answer(request, pk):
    answer = Answer.objects.get(pk=pk)
    Like.objects.get_or_create(answer=answer, user=request.user)
    return redirect('view_question', pk=answer.question.pk)
