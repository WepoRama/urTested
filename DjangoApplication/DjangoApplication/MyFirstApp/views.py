# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
import django.db
def getTest(intId):
    #Connect to the MySQL sample database 'world'
    cur = django.db.connections['local'].cursor()
    #Execute a trivial SQL query which returns the name of 
    #all countries contained in 'world'
    cur.execute("SELECT name from test")
    tmp = cur.fetchall()
    #Clean-up after ourselves
    cur.close()
    #if intId >= len(tmp):
    #    return "countries exhausted"
    return tmp[intId][0]

def home(request):
    return HttpResponse(render_to_string(
                                        'index.html',
                                        {'content': getTest(0)}
                                        ))