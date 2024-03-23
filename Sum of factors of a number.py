s=0
n=12
for i in range(1,n):
    if n%i==0:
        s=s+i
print(s)
if s>n:
    print("True")
else:
    print("Flase")