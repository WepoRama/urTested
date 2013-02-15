# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
import django.db
from models import Test
def getTest(intId):
    #Connect to the MySQL sample database 'world'
    #cur = django.db.connections['default'].cursor()
    #Execute a trivial SQL query which returns the name of 
    #all countries contained in 'world'
    #cur.execute("SELECT name from MyFirstApp_test")
    #tmp = cur.fetchall()
    #Clean-up after ourselves
    #cur.close()
    t = Test.objects.get(test_id=1)
    #if intId >= len(tmp):
    #    return "countries exhausted"
    return t.name
    #return tmp[intId][0]

def home(request):

    r = getTest(0)
    return HttpResponse(render_to_string(
                                        'index.html',
                                        {'content':r}
                                        ))