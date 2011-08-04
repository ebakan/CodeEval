#Multiples.py
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

    pairs=[[int(j) for j in i.split(",")] for i in data.split("\n")[:-1]]

    print "\n".join(str(lowestmult(i[0],i[1])) for i in pairs)
