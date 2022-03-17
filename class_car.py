class Car():

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def read(self):
        print(self.name+", "+self.brand)

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size=battery_size
    
    def desc_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def upgrade_battery(self,i_num):
        if self.battery_size<=70:
            self.battery_size+=i_num
            print("Your battery size had been added "+str(i_num)+"-kWh.")

class e_car(Car):
    def __init__(self,name,brand):
        super().__init__(name,brand)
        self.battery=Battery()

    def get_range(self):
        if self.battery.battery_size<=70:
            range=240
        elif self.battery.battery_size>=85:
            range=280
        
        print("You car can go approximately "+str(range)+" kilometers on a full charge.")

carcar=e_car('model s','tesla')
carcar.battery.upgrade_battery(20)
carcar.battery.desc_battery()
carcar.get_range()