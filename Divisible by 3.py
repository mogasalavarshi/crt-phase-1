a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
c = a+b
d = a-b
if (a%3==0 and b%3==0):
    print("They are divisible by 3")
    print(c)
else:
    print("They are not divisible by 3")
    print(d)