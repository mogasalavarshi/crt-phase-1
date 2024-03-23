math = int(input("Enter the math marks :"))
phy = int (input("Enter the phy marks :"))
chem = int (input("Enter the chem marks :"))
if (math>80) and (phy>80) and (chem>80):
    print("A+")
elif (60<math<80) and (60<phy<80) and (60<chem<80):
    print("B+")
else:
    print("Pass")