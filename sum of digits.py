n=12345
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)
