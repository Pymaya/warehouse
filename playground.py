'''
magicians=[
    'jack',
    'tom',
    'peter',
    'gwen',
]
def show_magician(magician):
    for magician in magicians:
        print(magician.title())

show_magician(magicians)

def make_great(magician):
    great_magicians=[]
    for magician in magicians:
        great_magicians.append(magician.title()+' the Great')
    return great_magicians

print(make_great(magicians))
print(magicians)
'''

'''
def get_toppings(size,*toppings):
    print("The following toppings would be added to your "+str(size)+"-inch pizza:\n")
    for topping in toppings:
        print('- '+str(topping).title())

get_toppings(12,12,'mushrooms','cheese')
'''

'''
def creat_user(username,**info):
    profile={}
    profile['username']=username
    for k,v in info.items():
        profile[k]=v
    return profile

print(creat_user('abercrombie',name='jack',desc='nnvv'))
'''

'''
def sw_toppings(topping):
    print(topping.title()+" will be added to you sandwich.")

sw_toppings("cheese")
sw_toppings("mushrooms")
'''

'''
def car_info(brand,model,**carinfo):
    info={}
    info['brand']=brand
    info['model']=model
    for k,v in carinfo.items():
        info[k]=v
    
    return info

a=car_info('benz','c300',color='white',tow_package='True')
for k,v in a.items():
    print(k+" is "+v)
'''
import class_user as c_u
a=c_u.User("peter","park",girlfriend="mary jane",age="19")
a.desc_user()