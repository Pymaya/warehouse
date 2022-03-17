class User():
    def __init__(self,f_name,l_name,**infos):
        self.f_name=f_name
        self.l_name=l_name
        self.login_attempts=0
        self.info={}
        for k,v in infos.items():
            self.info[k]=v
        
    def desc_user(self):
        print("First name is "+self.f_name.title()+".\nLast name is "+self.l_name.title()+".")
        for k,v in self.info.items():    
            print(k+" is "+v)

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

class Admin(User):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.privilege=Privileges()

    def desc_admin(self):
        self.privilege.desc_privilege()

class Privileges():
    def __init__(self):
        self.privilege=("add_user","remove_user","ban_user")

    def desc_privilege(self):
        for i in self.privilege:
            print(i,end=" ")

a=Admin('peter','park')
a.desc_admin()