# Main Function for scraping 
def murl(emotions): 
    urlhere="ERROR"
    emotion=emotions.lower()
    # IMDb Url for Drama genre of 
    # movie against emotion Sad 
    if(emotion == "sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Musical genre of 
    # movie against emotion Disgust 
    elif(emotion == "disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Family genre of 
    # movie against emotion Anger 
    elif(emotion == "anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Thriller genre of 
    # movie against emotion Anticipation 
    elif(emotion == "anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Sport genre of 
    # movie against emotion Fear 
    elif(emotion == "fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Thriller genre of 
    # movie against emotion Enjoyment 
    elif(emotion == "happy"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Western genre of 
    # movie against emotion Trust 
    elif(emotion == "trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Film_noir genre of 
    # movie against emotion Surprise 
    elif(emotion == "surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    return urlhere
  
