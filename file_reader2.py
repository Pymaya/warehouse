with open('learning_python.txt') as file_obj:
    contents=file_obj.readlines()

for line in contents:
    print(line.rstrip())