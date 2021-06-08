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

    question_csv = pd.read_excel('questions.xlsx', header=0, engine='openpyxl')
    question_cnt = question_csv.shape[0]
    for kth_question in range(question_cnt):
        q = Question(qtext=question_csv.loc[kth_question, 'qtext'],
                     qnumber=question_csv.loc[kth_question, 'qnumber'])
        q.save()

    random_user.question_cnt = question_cnt
    random_user.save()

    answers_csv = pd.read_excel('answers.xlsx', header=0, engine='openpyxl')
    for kth_question in range(answers_csv.shape[0]):
        a = Answer(atext=answers_csv.loc[kth_question, 'atext'],
                   qnumber=answers_csv.loc[kth_question, 'qnumber'],
                   anumber=answers_csv.loc[kth_question, 'anumber'],
                   q_to_ask=answers_csv.loc[kth_question, 'q_to_ask'])
        a.save()

    conseil_csv = pd.read_excel('conseils.xlsx', header=0, engine='openpyxl')
    for ith_conseil in range(conseil_csv.shape[0]):
        conseil_arguments = {'ctext': conseil_csv.loc[ith_conseil, 'ctext']}
        for kth_question in range(question_cnt):
            conseil_arguments['q' + str(kth_question + 1)] = conseil_csv.loc[ith_conseil, 'Q' + str(kth_question + 1)]
        c = Conseil(**conseil_arguments)
        c.save()


def homepage(request):
    define_all()
    return render(request, template_name='main/home.html')


def request_question(request):
    random_user = RandomUser.objects.get()
    for i in range(random_user.question_cnt):
        question_number = 'q' + str(i + 1)
        if getattr(random_user, question_number) == "Ask":
            return a_question(request, i + 1)
    return redirect('denoument')


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
            # update questions to ask
            q_to_ask = Answer.objects.get(anumber=answer_number).q_to_ask
            if q_to_ask[0] == "[":
                for qnumber_to_ask in eval(q_to_ask):
                    setattr(random_user, 'q' + str(qnumber_to_ask), "Ask")
            random_user.save()
            print('selected answer {} for question {}'.format(getattr(random_user, 'q' + str(qnumber)), qnumber))
        return redirect('request_question')


def denoument(request):
    random_user = RandomUser.objects.get()

    full_filter = {}
    for i in range(random_user.question_cnt):
        question_number = 'q' + str(i + 1)
        temp_filter = str(getattr(random_user, question_number))
        if "." in temp_filter:
            full_filter[question_number + "__in"] = ["<any>", temp_filter]
        elif temp_filter == "skip":
            full_filter[question_number + "__in"] = ["<any>"]
    conseils = list(Conseil.objects.filter(**full_filter))
    context = {'conseils': conseils}

    Question.objects.all().delete()
    Answer.objects.all().delete()
    Conseil.objects.all().delete()
    RandomUser.objects.all().delete()

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
            return redirect('accueil')
        else:
            return redirect('register')


def logoutpage(request):
    logout(request)
    return redirect('accueil')
