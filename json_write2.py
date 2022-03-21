import json

def get_stored_username():
    try:
        with open('uu.json') as f_obj:
            return json.load(f_obj)
    except:
        return None

def create_new_user():
    new_user=input("Please tell us your name: ")
    with open('uu.json','w') as f_obj:
        json.dump(new_user,f_obj)

def greet_user():
    flag=True
    gsu=get_stored_username()
    if gsu:
        while flag:
            user_check=input("Hi, are you "+gsu.title()+"?\n'y/n'")
            if user_check != 'y' and user_check != 'n':
                print("Please enter only 'y' or 'n'.")
                continue
            elif user_check=='n':
                create_new_user()
                print("Your username has been logged.")
                flag=False
            elif user_check=='y':
                print("Welcome back, "+gsu.title()+"!")
                flag=False
    else:
        create_new_user()

greet_user()