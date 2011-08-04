#Dupes.py
#Written by Eric Bakan

import sys
if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    print "\n".join([",".join([str(k) for k in set(int(j) for j in i.split(","))]) for i in data.split("\n")[:-1]])
