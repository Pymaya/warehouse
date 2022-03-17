class Restaurant():

    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.num_served=0

    def desc_restaurant(self):
        print("The restaurant's name is "+self.name.title()+". It serves "+self.cuisine_type.title()+" food.")

    def open_restaurant(self):
        print("The restaurant is now opening.")

    def set_num_served(self,num):
        '''set num of how many people will be served.'''
        self.num_served=num
        print(str(self.num_served)+" People will dine here.")

    def increment_num_served(self,i_num):
        self.num_served+=i_num
        print(str(self.num_served)+" People were served in our restaurant today.")

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type,*flavors):
        super().__init__(name,cuisine_type)
        self.flavor=flavors

    def desc_icf(self):
        for i in self.flavor:
            print(i,end=" ")

ics=IceCreamStand('kfc','fast food','sweet','spicy')
ics.desc_icf()