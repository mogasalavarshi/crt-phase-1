#Creating list using
#manual
list = [1,2,3,35,'Kareeem','paul','siva',325.20,'Nikitha','Komali','Ram','Pilli','Priya']
print(list)
#append
list.append ('suraj')
print(list)
#inserting
list.insert(5,'Lavanya')
print(list)
#for Loop Indexing
for i in range(0,len(list)):
    print(list[i])
    print(list[2:3])
    print(list[:5])
    print(list[::3])
#For Loops
for i in list:
    print(i)
for i in range(0,len(list),-2):
    print(list[i])

#slicing
print(list[:6:-4])
print(list[2:3])
print(list[:5])
print(list[::3])
#mutability
list[1]="SHA KHADHARI"
print(list)
