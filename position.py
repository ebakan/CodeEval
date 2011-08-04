#Bit Positions
#Written by Eric Bakan

import sys

def bitval(num,pos):
    return (num>>pos-1) & 1

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    nums=[[int(j) for j in i.split(",")] for i in data.split("\n")[:-1]]

    print "\n".join(["true" if bitval(i[0],i[1])==bitval(i[0],i[2]) else "false" for i in nums])

