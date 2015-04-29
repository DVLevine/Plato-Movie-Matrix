import gzip, operator
import matplotlib.pyplot as plt

#'productID','userID','profileName','helpfulness','score','time','summary','text'

def load_data():
    movie_reviews = []
    f = gzip.open('movies.txt.gz','rb').read(100000000)#100000000
    for data in f.split('\n\n'):
        movie_review = []
        index = 0
        for line in data.split('\n'):
            try:
                movie_review.append(line.split(': ',1)[1])
                index += 1
            except:
                pass
        if(index == 8):
            movie_reviews.append(movie_review)
    return movie_reviews

def avg_score(movie_reviews):
    scores = []
    for productID,userID,profileName,helpfulness,score,time,summary,text in movie_reviews:
        scores.append(float(score))

    #scores.sort(reverse=True) 
    avg_score = sum(scores)/len(scores)
    # plt.plot(scores)  
    # plt.ylabel('scores')
    # plt.show()
    print avg_score #4.09417639203

def richer_helpfulness_user(movie_reviews):
    helpfulnesses = {}
    for productID,userID,profileName,helpfulness,score,time,summary,text in movie_reviews:
        if userID not in helpfulnesses.keys():
            helpfulnesses[userID] = int(helpfulness.split('/')[0])
        else:
            helpfulnesses[userID] += int(helpfulness.split('/')[0])

    values = sorted(helpfulnesses.values())

    for i, j in helpfulnesses.iteritems():
        if j == values[-1]:
            print 'The most helpful user:', i # A2HYMA3BGE9ZHH

    print "His helpfulness:", values[-1] # max:  835
    print "# users with 0 helpfulness:", values.count(0) #0: 2982

    plt.plot(values,'bo')
    plt.title('The rich get richer: # helpfulness')
    plt.xlabel('users')  
    plt.ylabel('number of helpfulness')
    plt.show()

def richer_helpfulness_review(movie_reviews):
    helpfulnesses = []
    for productID,userID,profileName,helpfulness,score,time,summary,text in movie_reviews:
        helpfulnesses.append(int(helpfulness.split('/')[0]))
        
    values = sorted(helpfulnesses)

    print 'The most helpful review has', values[-1], 'reviews' 
    print "# reviews with 0 helpfulness:", values.count(0) #0: 2982

    plt.plot(values,'bo')
    plt.title('The rich get richer: review helpfulness')
    plt.xlabel('reviews')  
    plt.ylabel('number of helpfulness')
    plt.show()

    y = []
    for i in xrange(10):
        y.append(100*sum(values[len(values)/10*i:len(values)/10*(i+1)-1])/sum(values))
    y.append(100)
    x = [100/10*i for i in xrange(11)]
    plt.plot(x,y, x,x)
    plt.title('Lorenz curve of review helpfulness')
    plt.xlabel('cumulative % of reviews')
    plt.ylabel('cumulative % of helpfulness')
    plt.show()

def richer_num_reviews(movie_reviews):
    productID_array = []
    for productID,userID,profileName,helpfulness,score,time,summary,text in movie_reviews:
        productID_array.append(productID)

    productID_freq = {x:productID_array.count(x) for x in productID_array}
    sorted_freq = sorted(productID_freq.items(),key=operator.itemgetter(1))

    productIDs = [i[0] for i in sorted_freq]
    freq = [int(i[1]) for i in sorted_freq]
    
    print "The most reviewed movie:", productIDs[-1] # B000063W82
    print "Its # reviews:", freq[-1] # max:  589
    print "# movies with 0 review:", freq.count(0) 
    print "# movies with 1 review:", freq.count(1)#1:61, 
    print "# movies with 2 reviews:", freq.count(2)#2:42, 
    print "# movies with 3 reviews:", freq.count(3)#3: 24 #total: 127

    plt.plot(freq,'bo')
    plt.title('The rich get richer: # movie reviews')
    plt.xlabel('movies')  
    plt.ylabel('number of reviews')
    plt.show()

    y = []
    for i in xrange(10):
        y.append(100*sum(freq[len(freq)/10*i:len(freq)/10*(i+1)-1])/sum(freq))
    y.append(100)
    x = [100/10*i for i in xrange(11)]
    plt.plot(x,y, x,x)
    plt.title('Lorenz curve of number of reviews')
    plt.xlabel('cumulative % of movies')
    plt.ylabel('cumulative % of number of reviews')
    plt.show()


if __name__ == '__main__':
    movie_reviews = load_data()
    #print movie_reviews
    #richer_helpfulness_user(movie_reviews)
    richer_num_reviews(movie_reviews)
    richer_helpfulness_review(movie_reviews)
    '''
    dataset = 100000000 bytes
    The most helpful user: A328S9RN3U5M68
    His helpfulness: 1838
    # users with 0 helpfulness: 21912

    The most reviewed movie: B000VBJEFK
    Its # reviews: 770
    # movies with 0 review: 0
    # movies with 1 review: 529
    # movies with 2 reviews: 293
    # movies with 3 reviews: 202

    The most helpful review has 907 reviews
    # reviews with 0 helpfulness: 32446


    '''


