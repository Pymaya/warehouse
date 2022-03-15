class User():
    def __init__(self,f_name,l_name,**infos):
        self.f_name=f_name
        self.l_name=l_name
        self.info={}
        for k,v in infos.items():
            self.info[k]=v
        
    def desc_user(self):
        print("First name is "+self.f_name.title()+".\nLast name is "+self.l_name.title()+".")
        for k,v in self.info.items():    
            print(k+" is "+v)

a=User('peter','park',age='19',gender='male',girlfriend='Mary Jane')
a.desc_user()