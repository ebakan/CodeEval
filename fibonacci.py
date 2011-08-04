#Fibonacci Series
#Written by Eric Bakan

import sys

def memoizedFib(fiblist,num):
    if num<0:
	raise ValueError("Invalid number")
    while len(fiblist)<num+1:
	fiblist.append(fiblist[-1]+fiblist[-2])
    return fiblist[num]

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    nums=[int(i) for i in data.split("\n")[:-1]]

    fiblist=[0,1]

    print "\n".join([str(memoizedFib(fiblist,i)) for i in nums])
