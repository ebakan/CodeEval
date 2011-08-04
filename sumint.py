#Sum of Integers from File
#Written by Eric Bakan

import sys

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    print sum([int(i) for i in data.split("\n")[:-1]])
