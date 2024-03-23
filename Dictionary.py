dict={
    140:"Love",
    141:"Hate",
    142:"Drama",
    143:"Action"
}
print(dict)

#Mutability
dict[142]="Acting"
print(dict)

#Adding New key & Values
dict[144] = "Cinema"
print(dict)

#Accessing or Slicing
print(dict[140])

#For loops
for i in dict:  #prints keys
    print(i)
for i in dict.values():  #Prints values
    print(i)
for i,j in dict.items():  #Prints Keys & Values also
    print(i,j)

#Removing
dict.pop(142)
print(dict)