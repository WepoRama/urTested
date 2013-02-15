# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
import django.db
from models import Test
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

    r = getTest(0)
    return HttpResponse(render_to_string(
                                        'createTest.html',
                                        {'content':r}
                                        ))
