with open('pi.txt') as file_obj:
    contents=file_obj.read()
    file_obj.write(contents+'aabb')