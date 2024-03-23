a = int(input("Enter the  number :"))

if (a%3==0 and a%5==0):
    print("Great")
elif (a%3==0 and a%9==0):
    print("Good")
elif (a%3==0 and a%7==0):
    print("Ok")
else:
    print("Not Ok")