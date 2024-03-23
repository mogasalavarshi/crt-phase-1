def check(n):
    if n%10==5:
        return n**2
    elif n%10==3:
        return n**3
    elif n%10==6:
        return n-1
    else:
        return n/2
a= check(25)
print(a)
