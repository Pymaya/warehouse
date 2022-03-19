while True:
    r=input("Select mode: ")
    if r!='a' and r!='w' and r!='r':
        print("Only 'a' 'w' 'r' are available to enter.")
        continue
    else:
        break

with open('learning_python.txt',r) as file_obj:
    file_obj.write("\n456")






    '''
i learnt how to edit list.
i learnt how to edit tuple.
i learnt how to edit dict.
i learnt how to make a function.
i learnt how to make a class.
i learnt how to import funcitons and classes from other files or modules.
'''