def login():
    a=input("Enter the User name :")
    b=input("Enter the password :")
    if a==b:
        print("Successfully Logged in")
    else:
        print("Unsuccessful")
        print("Enter Again")
        login()
login()