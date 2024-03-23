class shopping:
    def dresstype (self,dt):
        self.s1 =dt
    def price (self,pr):
        self.s2 = pr
    def size (self,sz):
        self.s3 = sz
    def display (self):
        print(self.s1,self.s2,self.s3)
details = shopping()
details.dresstype("Cotton")
details.price(5000)
details.size("L")
details.display()

