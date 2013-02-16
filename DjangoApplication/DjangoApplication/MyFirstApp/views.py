# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
import django.db
from models import Test
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
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
    return render_to_response('createTest.html', #{'test_id': p},
                               context_instance=RequestContext(request))

def createIt(request):
    #p = get_object_or_404(Test)
    named = request.POST['name']
    authored = request.POST['author']
    expires = request.POST['expires']
    test = Test.objects.create( name = named, author = authored, expires_=expires)
    test.save()
    id = test.id()
    return render_to_response('addQuestion.html', {
            'test': test,
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

