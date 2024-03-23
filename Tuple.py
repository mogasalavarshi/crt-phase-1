#Creating a Tuple
#manually
tuple=("Kareem","Paul","Pilli","Siva Mutchakarla","Shekhar Master","Priya")
print(tuple)

print(type(tuple))
#Adding a Single Value to Tuple
tuple = tuple + ("Butterfly",)
print(tuple)
#Mutabality Checking
#tuple[2]="Tulasi"
#print(tuple)
##Adding Multiple Values to Tuple
tuple=tuple+("Saroja","Sweets","Gottam Kaja")
print(tuple)
#For Loop
for i in range(0,5):
    n=int(input("Enter the Values:"))
    tuple=tuple+(n,)
    print(tuple)