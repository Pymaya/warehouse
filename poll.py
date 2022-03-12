from def1 import display_msg
from def1 import favorite_book
from def1 import pets
from def1 import make_shirt
from def1 import describe_city
from def1 import build_person
from def1 import city_country
from def1 import make_album

while True:
    singer=input('Please enter a singer.\nenter "q" to quit.') # get singer name
    if singer=='q':
        break
    albumname=input('Please enter one ablum name of his.\nenter "q" to quit.') # get the album name
    if albumname=='q':
        break
    songs=input('How many songs does this album have?\nenter "q" to quit.') # get the songs amount of this album
    if songs=='q':
        break

    print(make_album(singer,albumname,songs))
