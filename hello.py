responses={}
polling=True

while polling:
    name=input('What is your name?')
    respond=input('Which mountain do you like the most?')
    responses[name]=respond
    repeat=input('Would you like to let others respond?')
    if repeat.lower()=='no':
        polling=False

print('---Poll Finished---')

for name,response in responses.items():
    print(name+' likes '+response+'.')