s=0
n=47
n1=n
while n1>0:
    d=n1%10
    s=s+d
    n1=n1//10
print(s)
if n%s==0:
    print("This is Divisible")
else:
    print("This is not divisible")