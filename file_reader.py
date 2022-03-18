
with open('pi.txt') as file_obj:
#    lines=file_obj.readlines()

#pi_str=''
#for line in lines:
#    pi_str+=line.rstrip()
    contents=file_obj.read()

b_day=input("Enter your birthday in format mmddyy: ")
if b_day in contents:
    print("it's in it.")
else:
    print("it's not in it.")

index=contents.find(b_day)
print(str(index))