import sys, os                                                                                                                                                                                  
sys.path.append('/root/TheMatrix/TheMatrix/TheMatrix')                                                                                                                                          
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'                                                                                                                                              
from django.conf import settings    
from Plato.models import *
from pymongo import MongoClient
from textblob import TextBlob

#import Plato.models


def loadPerception():
    client = MongoClient()                                                                                                                                                                      
    db = client.plato_test                                                                                                                                                                      
    collection = db.review                                                                                                                                                                      
    theList = []                                                                                                                                                                               
    presentTotal = 0
    presentPol = 0
    presentSub = 0
    count = 1
    # Have dictionary keep track of duplicates. skip them if dup. up count until get at least 10 unique                                                                                         
    dupCheck = set([])    
    movCheck = set([])

    Percy = collection.find(no_cursor_timeout=True)
    for review in Percy:
        if (review["user_id"] in dupCheck):
            continue
        else:
            dupCheck.add(review["user_id"])
            userID = review["user_id"]
            snake = collection.find({"user_id":userID}) 
            bob = snake.sort("time")
            
            for ele in bob:
                if (ele["movie_id"] in movCheck):
                    continue
                else:
                    movCheck.add(ele["movie_id"])
                    # get movieIDs. 
                    #print ele
                    print "YOOOOOOOOOOOOOOO" + str(count)
                    sum_text = ele["summary"]                                                                                                                                                   
                    text =  ele["full_text"]                                                                                                                                                 
                    blob = TextBlob(text)                                                                                                                          
                    sumBlob = TextBlob(sum_text)  


                    presentTotal += ele["score"]                                                                                                                               
                    presentPol += sumBlob.sentiment.polarity
                    presentSub += sumBlob.sentiment.subjectivity

                    presentAvg = presentTotal/count
                    presentPAvg = presentPol/count
                    presentSAvg = presentSub/count
    
                    entry = unitPerception(movie_id=ele["movie_id"],score = ele["score"], adjustedScore = ele["score"])                                                                
                    theList.append(entry)                                                                                                                         
                    count +=1 
                        
            if avg_polarity != 0:
                perceptionEntry = Perception(user_id = userID, avg_polarity= presentPAvg, avg_subjectivity= presentSAvg, avg_score = presentAvg,elements = theList)       
                perceptionEntry.save()                                                                                                                                                             
            theList = []                                                                                                                                                                        
            count = 1                                                                                                                                                                           
            presentTotal = 0
            presentPol = 0
            presentSub = 0

def loadAnchoring():
    client = MongoClient()                                                                                                                                                                    
    db = client.plato_test                                                                                                                                                                     
    collection = db.review      
    theList = []
    presentTotal = 0
    count = 1
    # Have dictionary keep track of duplicates. skip them if dup. up count until get at least 10 unique
    dupCheck = set([])

    Bob = collection.find(no_cursor_timeout=True)#.limit(10000)

    for review in Bob:
        if (review["movie_id"] in dupCheck):
            continue
        else:
            dupCheck.add(review["movie_id"])
            movieID = review["movie_id"] 
            snake = collection.find({"movie_id": movieID})#.distinct("time") 
            if snake.count() < 100:
                print("Skipped")
                continue
            else:
                print ("GO!")
                bob = snake.sort("time") 
                #bob = snake#.__getitem__
                #collection.find({"movie_id": movieID})
        
                for ele in bob:
                    #print ele
                    #print "GOOOOOOOOOOOOOOOOOO "+str(count) 
                    presentTotal += ele["score"]
                    presentAvg = presentTotal/count
                    
                    entry = unitAnchoring(time = ele["time"], present_avg_score = presentAvg, most_recent_ind_score = ele["score"])
                    theList.append(entry)
                    count +=1
        
                anchorEntry = Anchoring(movie_id = movieID, elements = theList)
                anchorEntry.save()
                theList = []
                count = 1
                presentTotal = 0

def loadRicher():
    client = MongoClient()                                                                                                                                                                      
    db = client.plato_test                                                                                                                                                                      
    collection = db.review                                                                                                                                                                     
    theList = []
    presentTotal = 0
    helpfulNum = 0
    helpfulDen = 0
    count = 1                                                                                                                                                                                   
    # Have dictionary keep track of duplicates. skip them if dup. up count until get at least 10 unique                                                                                         
    dupCheck = set([]) 
    movCheck = set([])
    Richie = collection.find(no_cursor_timeout=True)
    for review in Richie:                                                                                                                                                                       
        if (review["user_id"] in dupCheck):                                                                                                                                                     
            continue                                                                                                                                                                            
        else:                                                                                                                                                                                   
            dupCheck.add(review["user_id"])                                                                                                                                                     
            userID = review["user_id"]                                                                                                                                                          
            snake = collection.find({"user_id":userID})                                                                                                                                         
            presentTotal = snake.count()
            #bob = snake.sort("time")                                                                                                                                                           
            for ele in snake:                                                                                                                                                                   
                if (ele["movie_id"] in movCheck):                                                                                                                                               
                    continue                                                                                                                                                                    
                else:                                                                                                                                                                           
                    movCheck.add(ele["movie_id"])                                                                                                                                               
                    # get movieIDs.                                                                                                                                                             
                    #print ele                                                                                                                                                                 
                    print "YOOOOOOOOOOOOOOO" + str(count) 
                    helpfulNum += int((str.split(ele["helpfulness"].encode('ascii','ignore'), "/"))[0])
                    helpfulDen += int((str.split(ele["helpfulness"].encode('ascii','ignore'), "/"))[1])
                count += 1
            entry = bestHuman(user_id = ele["user_id"],numMovies = presentTotal, mostHelped=helpfulNum, totalHelped=helpfulDen) 
            entry.save()
            count = 1
            helpfulNum = 0
            helpfulDen = 0
            
def sentiment():
    doob = "Great Movie!"    
    blob = TextBlob(doob)

    for sentence in blob.sentences:
        print(sentence.sentiment)
        
    print blob.translate(to="cn") 


def other():
    client = MongoClient()
    db = client.plato_test
    collection = db.review

    for doob in collection.find().limit(5):

        #userID = collection.find_one()["user_id"]
        userID = doob["user_id"]
        movieID = doob["movie_id"]
        print "**************** " + userID + " ****************"
        for ele in collection.find({"movie_id": movieID}).limit(10):
            print ("--------------------------\n")
        
            #       print count
            sum_text = ele["summary"]
            text =  ele["full_text"]
            print sum_text
            print text
            blob = TextBlob(text)
            sumBlob = TextBlob(sum_text)
            
            print "Header Polarity: " + str(100*sumBlob.sentiment.polarity) + "%"
            print "Header Subjectivity: " + str(100*sumBlob.sentiment.subjectivity) + "%"

            print "Review Polarity: " + str(100*blob.sentiment.polarity) + "%" 
            print "Review Subjectivity: " + str(100*blob.sentiment.subjectivity) + "%"

            print "Rating: " + str(ele["score"])
            print "Helpfulness: " + ele["helpfulness"]
            #print blob.sentences
            #%print blob.translate(from_lang='en', to="zh-CN")
            #      count +=1
            #print collection.find_one({"helpfulness": "10/10\n"})  
            pol_avg = 0
            subj_avg = 0
            summary_avg = 0
'''
def query():
    count = 0
    Dood = Review.objects
    for ele in Dood:     
        if isinstance(ele, Review):
            print ele.summary
            print count
        else:
            print NONONO
#        print ele.summary
        count +=1
 #       print ele.helpfulness
  #      print ele.full_text
    #    print ele.user_id  
    print Review.objects.count()
    #print Review.objects.
'''


if __name__ == "__main__":                                                                                                                                                                     
    print "HEY DUDE"                                                                                                                                                                     
    #query()
    #other()
    #sentiment()
#    loadPerception()
    loadRicher()
# **** REAL THINGS
#    loadAnchoring()
