import json

def desc_fnum():
    try:
        with open('f_num.json') as fobj:
            favorite_number=json.load(fobj)
            print('Your favorite number is '+favorite_number)
    
    except:
        f_number=input("Please tell me your favorite number: ")
        with open('f_num.json','w') as fobj2:
            json.dump(f_number,fobj2)

desc_fnum()