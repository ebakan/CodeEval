#Fizzbuzz.py
#Written by Eric Bakan

import sys

def fizzbuzz(tup):
    a=tup[0]
    b=tup[1]
    n=tup[2]
    return " ".join(["FB" if i%a==0 and i%b==0 else "F" if i%a==0 else "B" if i%b==0 else str(i) for i in range(1,n+1)])

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    print "\n".join([fizzbuzz([int(j) for j in i.split(" ")]) for i in data.split("\n")[:-1]])
