‘’‘
from mergedict import mergedict
test_a={
    'name':'jack',
    'age':'19',
    'weight':'70kg',
    'gender':'male',
}
f_1=test_a.keys()
f_2=test_a.values()

vv={}
vv=mergedict(f_1,f_2)

print(vv)
’‘’

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
