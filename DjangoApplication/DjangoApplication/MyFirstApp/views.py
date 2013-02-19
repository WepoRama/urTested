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
def getTest(intId):
    t = Test.objects.get(test_id=1)
    return t.name

def home(request):
    r = getTest(0)
    return HttpResponse(render_to_string(
                                        'index.html',
                                        {'content':r}
                                        ))
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
    return render_to_response('choose.html', {
            },
        context_instance=RequestContext(request)
        )

    #try:
    #    selected_choice = p #.choice_set.get(pk=request.POST['choice'])
    #except (KeyError, Choice.DoesNotExist):
    #    # Redisplay the poll voting form.
    #    return render_to_response('polls/detail.html', {
    #        'poll': p,
    #        'error_message': "You didn't select a choice.",
    #    }, context_instance=RequestContext(request))
    #else:
    #    selected_choice.votes += 1
    #    selected_choice.save()
    #    # Always return an HttpResponseRedirect after successfully dealing
    #    # with POST data. This prevents data from being posted twice if a
    #    # user hits the Back button.
    #    return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

