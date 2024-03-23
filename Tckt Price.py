tckt = int(input("Enter the price of the ticket :"))

if tckt>=250 and tckt<=300:
    print("Recliners")
elif tckt>=200 and tckt<=250:
    print("Platinum")
elif tckt>=150 and tckt<=200:
    print("Glod")
elif tckt>=100 and tckt<=150:
    print("Silver")
else:
    print("Balcony")