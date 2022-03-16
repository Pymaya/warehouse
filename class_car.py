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

class e_car(Car):
    def __init__(self,name,brand):
        super().__init__(name,brand)
        self.battery=Battery()

carcar=e_car("model s","tesla")
carcar.read()
carcar.battery.desc_battery()