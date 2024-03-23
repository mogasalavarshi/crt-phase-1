def login():
    n=1
    # while n!=0:
    while True: 
        a=input("Enter the User Name :")
        b=input("Enter the Password :")
        if a==b:
            print("Succesfully Logged in")
            break
        else:
            print("Invalid Enter Again")
login()