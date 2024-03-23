def is_prime():
    f=1
    n=int(input("Enter the Number:"))
    for i in range(2,n):
        if n%i==0:
             f=0
             break
    if f==1:
        print("It is Prime")
    else:
        print("It is not prime")
is_prime()