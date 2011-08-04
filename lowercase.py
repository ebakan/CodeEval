#Lowercase
#Written by Eric Bakan

import sys

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    lowercase=data.lower()
    sys.stdout.write(lowercase)
