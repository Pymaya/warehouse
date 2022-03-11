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
