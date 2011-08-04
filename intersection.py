#Set Intersection.py
#Written by Eric Bakan

import sys

def lowestmult(a,b):
    out=b
    while(out<a):
	out+=b
    return int(out)

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    sets=[[j.split(",") for j in i.split(";")] for i in data.split("\n")[:-1]]
    
    print "\n".join([",".join([j for j in i[0] if j in i[1]]) for i in sets])
