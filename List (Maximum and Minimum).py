mylist = [42,36,28,96,4,-1,1]
mini = 999
for i in range (0,len(mylist)):
    if (mylist[i]< mini):
        mini=mylist[i]
print("The minimum value among the given list :",mini)
maxi = -999
for i in range (0,len(mylist)):
    if (mylist[i]> maxi):
        maxi=mylist[i]
print("The maximum value among the given list :",maxi)
sum = maxi+mini
print ("The Sum of the maximum and minimum value is:",sum)
 