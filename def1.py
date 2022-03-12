def display_msg():
    print("I learnt how to make a function in this chapter.")

def favorite_book(bookname):
    print("My favorite book is "+str(bookname).title()+".")

def pets(pet_type,pet_name):
    print("I have a "+pet_type+". Its name is "+pet_name)

def make_shirt(size,content='I love Python'):
    print("Your shirt would be in size '"+size+"' with content '"+content+"' on it.")

def describe_city(name,country='china'):
    print(str(name).title()+" is in "+str(country).title()+".")

def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person

def city_country(city,country):
    a=city.title()+', '+country.title()
    return a

def make_album(singer,a_name,songs=''):
    a={}
    a['singer']=singer
    a['album_name']=a_name # add singer and album name to dict
    
    if songs:
        a['songs']=songs # add songs amount to dict if any
    
    return a
