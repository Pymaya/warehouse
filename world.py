sandwich_orders=[
    'tuna',
    'cheese',
    'pastrami',
    'beef',
]
finished_sandwiches=[]

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("Sorry, pastrami is sold out.")


while sandwich_orders:
    temp_=sandwich_orders.pop()
    print('I made your '+temp_.title()+' sandwich.')
    finished_sandwiches.append(temp_)

for sandwich in finished_sandwiches:
    print(sandwich.title()+' sandwich is done.')