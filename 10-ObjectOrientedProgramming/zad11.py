class Tv():
    def __init__(self, brand, year, size):
        self.brand=brand
        self.year=year
        self.size=size
        self.is_on=False
        self.channel_no=1
        self.avalchan=[]
        self.volume=0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def set_channel(self, channelnum):
        self.channel_no=channelnum
    def set_channels(self,channeladd):
        self.avalchan.append(channeladd)
    def show_channels(self):
        for channel in range(len(self.avalchan)):
            print(f'{channel+1}. {self.avalchan[channel]}')
    def increase_vol(self, num):
        if self.volume>10:
           self.volume+=num
        else:
            print("Max volume reached")
    def decrease_vol(self,num):
        if self.volume>0:
          self.volume-=num
        else:
            print("Min volume reached")
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else: 
            print("TV is off")
        print(f"The current volume is: {self.volume}")
    



tv=Tv("LG",2023,"6")

tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.show_channels()
tv.set_channels("TVP1")
tv.show_channels()
tv.show_status()
tv.turn_off()
tv.show_status()
tv.increase_vol(12)
tv.show_status()



    

        