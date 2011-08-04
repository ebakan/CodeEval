#Multiplication Tables.py
#Written by Eric Bakan

print "\n".join([''.join([str(i*j).rjust(4) for j in range(1,13)]) for i in range(1,13)])
