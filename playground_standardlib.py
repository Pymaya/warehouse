from collections import OrderedDict

test=OrderedDict()
test['name']='peter park'
test['gender']='male'
test['age']='19'

for k,v in test.items():
    print(k.title()+" "+v.title())

test2={}
test2['name']='peter park'
test2['gender']='male'
test2['age']='19'

for k2,v2 in test2.items():
    print(k2.title()+" "+v2.title())