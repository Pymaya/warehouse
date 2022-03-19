def count_words(word):
    with open("siddhartha.txt", encoding='utf-8') as f_obj:
        contents=f_obj.read()
        wordnum=len(contents.split())
        freq=str((contents.lower().count(word)/wordnum)*100)+"%"
        return freq
    
a=count_words('quit')
print(a)