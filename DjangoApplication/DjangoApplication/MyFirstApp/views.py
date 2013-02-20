# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
import django.db
from models import Test
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from DjangoApplication.MyFirstApp.models import Question, Score
from DjangoApplication.MyFirstApp.models import Answer
import locale
from datetime import date

def createTest(request):
    return render_to_response('createTest.html', 
                               context_instance=RequestContext(request))
def createIt(request):
    #p = get_object_or_404(Test)
    named = request.POST['name']
    authored = request.POST['author']
    expiresDate = request.POST['expires']
    test = Test.objects.create( name = named, author = authored, expires=expiresDate)
    test.save()
    id = test.id
    ret = render_to_response('addQuestion.html', {
            'test': test,
            },
        context_instance=RequestContext(request)
        )
    return ret
def addQuestion(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    ask = request.POST['question']
    points = request.POST['points']
    question = Question.objects.create( question=ask, points=points, test=test)
    question.save()
    return render_to_response('addQuestion.html', {
            'test': test,
            'current': question,
            },
        context_instance=RequestContext(request)
        )
def addAnswer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #test = Test.objects.get( test_id=question.test_id)

    answer = request.POST['answer']
    try:
        correct = request.POST['correct']
    except:
        correct=False
    anAnswer = Answer.objects.create( question=question, answer=answer, correct=correct)
    anAnswer.save()
    return render_to_response('addQuestion.html', {
            'test': question.test,
            'current': question,
            },
        context_instance=RequestContext(request)
        )
def takeTest(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return render_to_response('takeTest.html', {
            'test': test,
            },
        context_instance=RequestContext(request)
        )
def rateTest(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    scored = 0
    for item in test.question_set.all():
        qid = locale.format("%d", item.id)
        ans = request.POST[qid]
        check = Answer.objects.get(id = ans )
        if check.correct:
            question = check.question
            scored += question.points
    name = request.POST['name']
    score = Score.objects.create( score=scored, test=test, name=name)
    score.save()
    return render_to_response('rateTest.html', {
            'test': test,
            'score': score,
            },
        context_instance=RequestContext(request)
        )
def choose(request):
    if request.user.has_perm('MyFirstApp.add_test'):
        return render_to_response('createTest.html', {
            },
        context_instance=RequestContext(request)
        )
    else:
        return listTests(request)
def listTests(request):
    allTests = Test.objects.all().filter()
    tests = allTests.exclude( expires__lt =  date.today() )     
    return render_to_response('listTests.html', {
            'tests': tests,
        },
    context_instance=RequestContext(request)
    )
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    txt = request.POST['login']
    txt = request.POST['next']
    if user is not None:
        if user.is_active:
            login(request, user)
            #if user.
            return render_to_response('choose.html')
       #else:
            # Return a 'disabled account' error message
        #else:
            # Return an 'invalid login' error message.
