
from pickle import dump,load


def write(fname,obj):
    file=open(fname,"wb")
    dump(obj,file)
    file.close()

def read(fname):
    try:
        file=open(fname,"rb")
        z=load(file)
        file.close()
    except:
        z=[]
    return z
 