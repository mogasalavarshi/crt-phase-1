class car:
    def company(self,name):
        l=['toyota','mercedes','suzuki']
        if name in l:
            print("welcome to",name)
    def model(self,name):
        d={'toyota':['fortuner','innova'],
'mercedes':['bmw'],'suzuki':['swift','alto']}
        if name in d:
             print(d[name])
    def price(self,name,m):
        print("you have selected",m)
        prices_list={'fortuner':7500000,
'innova':5000000,'bmw':10000000,
'swift':300000,'alto':100000}
        if m in prices_list:
            car_prices=prices_list[m]
            gst=0.1*car_price
            insurance=100000
            final_price=car_price+gst+insurance
            print("final price:",final_price)
n=input("enter the car company:")
c=car()
c.company(n)
m=input("enter model of car:")
c.price(n,m)
