R=5
for i in range(1,6):
    for s in range(1,R-i+1): #for space priting
        print(" ",end="")
    for j in range(1,i+1): #for pattren priting
        print("*",end="")
    print()