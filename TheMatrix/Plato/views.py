# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.template import Template
import datetime

from Plato.models import *                                                                                                                                                                 
from pymongo import MongoClient                                                                                                                                                                

def PostCreateView(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    client = MongoClient()
    db = client.plato_test
    string = "hello doods"
    template = loader.get_template('home.html')
    context = Context({"homely":string})
    return HttpResponse(template.render(context))

def anchoring(request):
    client = MongoClient()                                                                                                                                                                      
    db = client.plato_test 
    anchorings = db.anchoring.find()
    template = loader.get_template('anchoring.html')                           
    context = Context({"anchors":anchorings})                 
    return HttpResponse(template.render(context))  

def perception(request):
    client = MongoClient()
    db = client.plato_test
    perceptions = db.perception.find().sort('avg_score')
    template = loader.get_template('perception.html')                          
    context = Context({"perceptions":perceptions})                 
    return HttpResponse(template.render(context))  

def richer(request):
    client = MongoClient()
    db = client.plato_test
    #lor = db.lorenz.find_one()
    #humans = db.best_human.find().sort('sortField')
    sums = db.sums.find_one()["richSum"]
    runSnaps = db.run_snap.find().sort('runSnap')
    cumSnaps = db.cum_snap.find().sort('cumSnap')
    
#    cumSum = db.help_sum.find().limit(10000).sort('helpSum',-1)



    #pipeline = [{"$unwind": "$tags"},{"$group": {"_id": "$numHelped", "count": {"$sum": 1}}},{"$sort": SON([("count", -1), ("_id", -1)])}]

# list(db.richer.aggregate(pipeline))

#    richers = db.richer.find().limit(10000).sort('numHelped',-1)
    template = loader.get_template('richer.html')                              
    context = Context({ "sums": sums, "runSnaps": runSnaps, "cumSnaps":cumSnaps})                 
    return HttpResponse(template.render(context))  
