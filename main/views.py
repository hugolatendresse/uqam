from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Question, Answer, RandomUser, Conseil


def define_all():
    Question.objects.all().delete()
    Answer.objects.all().delete()
    RandomUser.objects.all().delete()
    random_user = RandomUser()
    random_user.save()
    q1 = Question(qtext="De quel pays venez-vous?", qnumber=1)
    q1.save()
    q2 = Question(qtext="Etes-vous au Canada en ce moment", qnumber=2)
    q2.save()
    a1 = Answer(atext="France", qnumber=1, anumber=1)
    a1.save()
    a2 = Answer(atext="Autre", qnumber=1,anumber=2)
    a2.save()
    a3 = Answer(atext='Oui', qnumber=2, anumber=1)
    a3.save()
    a4 = Answer(atext='Non', qnumber=2, anumber=2)
    a4.save()


def homepage(request):
    define_all()
    return render(request, template_name='main/home.html')


def request_question(request):
    random_user = RandomUser.objects.get()
    if random_user.q1 == "Ask":
        return a_question(request, 1)
    elif random_user.q2 == "Ask":
        return a_question(request, 2)
    else:
        return denoument(request)


def a_question(request, qnumber):
    # messages.success(request, "This is a django message")
    question = Question.objects.get(qnumber=qnumber)
    reponses = list(Answer.objects.filter(qnumber=qnumber))
    if request.method == "GET":
        return render(request, template_name='main/questions_v2.html', context={'question': question, 'responses': reponses})
    elif request.method == "POST":
        answer_number = request.POST.get('answer_number')
        if answer_number:
            random_user = RandomUser.objects.get()
            setattr(random_user, 'q' + str(qnumber), str(answer_number))
            random_user.save()
            print('selected answer {} for question {}'.format(getattr(random_user, 'q' + str(qnumber)), qnumber))
        return redirect('request_question')


def denoument(request):
    random_user = RandomUser.objects.get()
    conseil = Conseil(text=str([random_user.q1, random_user.q2]))
    context = {'conseil': conseil}
    return render(request, template_name='main/denoument.html', context=context)


def loginpage(request):
    if request.method == "GET":
        return render(request, template_name='main/login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('a_question')
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


