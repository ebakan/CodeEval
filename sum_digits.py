#Sum of Digits
#Written by Eric Bakan

import sys

def sumDigits(num):
    s=0
    while(num!=0):
	s+=num%10
	num/=10
    return s

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    lines=data.split("\n")[:-1]
    ints=[int(i) for i in lines]
    sums=[sumDigits(i) for i in ints]

    print "\n".join([str(i) for i in sums])
