import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Question, Answer, RandomUser, Conseil


def define_all():
    Question.objects.all().delete()
    Answer.objects.all().delete()
    Conseil.objects.all().delete()
    RandomUser.objects.all().delete()
    random_user = RandomUser()
    random_user.save()

    question_csv = pd.read_csv('questions.csv', header=0)
    for i in range(question_csv.shape[0]):
        q = Question(qtext=question_csv.loc[i, 'qtext'],
                     qnumber=question_csv.loc[i, 'qnumber'])
        q.save()

    answers_csv = pd.read_csv('answers.csv', header=0)
    for i in range(answers_csv.shape[0]):
        a = Answer(atext=answers_csv.loc[i, 'atext'],
                   qnumber=answers_csv.loc[i, 'qnumber'],
                   anumber=answers_csv.loc[i, 'anumber'],
                   q_to_skip=answers_csv.loc[i, 'q_to_skip'])
        a.save()

    conseil_csv = pd.read_csv('conseils.csv', header=0)
    for i in range(conseil_csv.shape[0]):
        c = Conseil(ctext=conseil_csv.loc[i, 'ctext'],
                    q1=conseil_csv.loc[i, 'Q1'],
                    q2=conseil_csv.loc[i, 'Q2'],
                    )
        c.save()


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
            # update answer
            setattr(random_user, 'q' + str(qnumber), str(answer_number))
            # update questions to skip
            q_to_skip = Answer.objects.get(anumber=answer_number).q_to_skip
            if q_to_skip[0] == "[":
                for qnumber_to_skip in eval(q_to_skip):
                    setattr(random_user, 'q' + str(qnumber_to_skip), "skip")
            random_user.save()
            print('selected answer {} for question {}'.format(getattr(random_user, 'q' + str(qnumber)), qnumber))
        return redirect('request_question')


def denoument(request):
    random_user = RandomUser.objects.get()

    QUESTION_COUNT = 2

    full_filter = {}
    for i in range(QUESTION_COUNT):
        question_number = 'q' + str(i+1)
        temp_filter = str(getattr(random_user, question_number))
        if "." in temp_filter:
            full_filter[question_number+"__in"] = ["<any>", temp_filter]
        elif temp_filter == "skip":
            full_filter[question_number + "__in"] = ["<any>"]
    conseils = list(Conseil.objects.filter(**full_filter))
    context = {'conseils': conseils}
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
