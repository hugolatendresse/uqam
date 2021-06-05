from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Question, Answer



def homepage(request):
    return render(request, template_name='main/home.html')


def Q1(request):
    messages.success(request, "This is a django message")
    q1_instance = Question(qtext="De quel pays venez-vous?")
    a1 = Answer(atext="France")
    a2 = Answer(atext="Autre")
    # q1_instance.save()
    reponses = [a1, a2]
    if request.method == "GET":
        return render(request, template_name='main/questions_v2.html', context={'question': q1_instance, 'responses': reponses})
    # elif request.method == "POST":
    #     purchased_item = request.POST.get('purchased-item')
    #     if purchased_item:
    #         purchased_item_object = Item.objects.get(name=purchased_item)
    #         purchased_item_object.owner = request.user
    #         purchased_item_object.save()
    #         print('congrats the new user ({}) is saved for {}'.format(request.user.username, purchased_item))
    #     return redirect('Q1')


def loginpage(request):
    if request.method == "GET":
        return render(request, template_name='main/login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Q1')
        else:
            return redirect('login')


def registerpage(request):
    if request.method == "GET":
        return render(request, template_name='main/register.html')
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')


def logoutpage(request):
    logout(request)
    return redirect('home')
