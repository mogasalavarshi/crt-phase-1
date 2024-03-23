class F15:
    def light(self):
        print("Ok Switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is ",speed)
        self.s = speed
    def cpu(self):
        print("Powering on the system")
        print(self.s)

chandu = F15()
chandu.light()
chandu.fan(5)
chandu.cpu()