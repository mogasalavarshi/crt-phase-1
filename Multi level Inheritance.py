class F15:
    def light(self):
        print("Ok Switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is ",speed)    #A class
        self.s = speed
    def cpu(self):
        print("Powering on the system")
        print(self.s)

chandu = F15()
class shopping(F15):
    # def __init__(self,place):
    #     self.place=place
    #     print("Welcome to shopping at ",place)     #B class
    def dresstype (self,dt):
        self.s1 =dt
    def price (self,pr):
        self.s2 = pr
    def size (self,sz):
        self.s3 = sz
    def display (self):
        print(self.s1,self.s2,self.s3)
# details = shopping("Raymond")
class pragati(shopping):
    def branch (self,br):
        self.s4=br
    def section (self,sec):
        self.s5=sec
    def rollnumber(self,roll):
        self.s6=roll
    def display1 (self):
        print(self.s4,self.s5,self.s6)
details1 =pragati()
details1.dresstype("Cotton")
details1.price(5000)
details1.size("L")
details1.display()
details1.light()
details1.fan(5)
details1.cpu()
details1.branch("ECE")
details1.section("E")
details1.rollnumber("21A31A04U8")
details1.display1()
