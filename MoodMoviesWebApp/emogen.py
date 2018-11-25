happylist=["happy","happiness","cheerfull","cherry","joyfull","joy","jolly","glowing","joyous","buoyant","delighted","lucky","satisfied","blessed"]
fearlist=["terror","fight","horror","panic","agitation","dread","distress","fear"]
angerlist=["annoyance","vexation","irritation","displeasure","resentment","annoy","anger","angry","displease"]
sadlist=["unhappy","sorrowfull","dejected","regretful","depressed","gloomy","brokenhearted","heartbroken","sad","sadness"]
disgustlist=["revulsion","disgust","aversion","odium","repel","revolt","repulse","sicken"]
surpriselist=["shock","suprise","thunderbolt","bombshell","astonish","amaze","stun","astound"]
trustlist=["trust","confidence","belief","faith","certainity","assurance","reliance"]
shamelist=["shame","humiliation","mortification","embarrassment","indignity","ignominy"]
excitementlist=["excitement","exhilaration","anticipation","thrill","adventure","treat","eagerness","enthusiasm"]
pridelist=["pride","delight","joy","satisfaction","dignity","honour","selfrespect","gratification"]

def ea(emotion):
    emotion=emotion.lower()
    if(emotion in happylist):
        return "comedy"
    elif(emotion in sadlist):
        return "crime"
    elif(emotion in fearlist):
        return "horror"
    elif(emotion in angerlist):
        return "war"
    elif(emotion in disgustlist):
        return "drama"
    elif(emotion in surpriselist):
        return "mystery"
    elif(emotion in trustlist):
        return "romance"
    elif(emotion in shamelist):
        return "shame"
    elif(emotion in pridelist):
        return "sci-fi"
    elif(emotion in excitementlist):
        return "adventure"
    else:
        return "Other"
