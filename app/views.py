

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm, UserRegisterForm
from . models import Question, Answer, Vote
from django.urls import reverse


def custom_logout(request):
    logout(request)
    return redirect(to="app:login")


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.warning(
                request=request, message="Invalid login credentials!"
            )
            return redirect(to="app:login")
        login(request, user)
        return redirect(to="app:home")

    return render(request=request, template_name="login.html")


@login_required
def home(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "home.html", {"questions": questions})


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            messages.success(
                request, "Your account has been created ! You are now able to log in"
            )
            return redirect("app:login")
        return render(request, "signup.html", {"form": form})

    form = UserRegisterForm()
    return render(
        request, "signup.html",
        {
            "form": form,
            "title": "register here"
        }
    )


@login_required
def question(request, pk=None):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, "success")
            return redirect(reverse("app:home"))
        return render(
            request, "post_question.html",
            {
                "form": form
            }
        )
    elif pk:
        question = Question.objects.get(pk=pk)
        user_list = question.answers_to_question.all().values_list(
            "user", flat=True
        )
        print("UYGBUBINIHMJ", question.answers_to_question.all().values())
        return render(
            request, "home.html",
            {
                "question": question,
                "users": user_list
            })
    form = QuestionForm()
    return render(
        request, "post_question.html",
        {
            "form": form,
            "title": "Question"
        })


@login_required
def answer(request, pk=None):
    if request.method == "POST" and pk:
        question = Question.objects.get(pk=pk)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            messages.success(request, "success")
            return redirect(reverse("app:question", kwargs={"pk": pk}))
        messages.error(request, "success")
        return redirect(reverse("app:question", kwargs={"pk": pk}))
    return redirect(reverse("app:question"))


@login_required
def vote(request, pk):
    if request.method == "POST":
        answer = Answer.objects.get(pk=pk)
        _, created = Vote.objects.get_or_create(
            answer=answer,
            user=request.user
        )
        print("UFYBGINHBYNHU", pk)
        print("UFYBGINHBYNHU", _)
        print("UFYBGINHBYNHU", created)
        print("UFYBGINHBYNHU", answer)
        if created:
            messages.success(request, "success")
            return redirect(
                reverse("app:question", kwargs={"pk": answer.question.id})
            )
        messages.error(request, "Already answerd")
        return redirect(
            reverse("app:question", kwargs={"pk": answer.question.id})
        )
    messages.error(request, "Invalid id")
    return redirect(reverse("app:question", kwargs={"pk": answer.question.id}))
