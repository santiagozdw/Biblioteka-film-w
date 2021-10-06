from typing import ItemsView
from Film import Film
from Serial import Serial
from random import randint
from datetime import datetime

#1.
print("Biblioteka filmów")
#2.
library = [
    Film(title='Pulp Fiction', year=1994, type='Film', views=0),
    Film(title='Pulp Fiction2', year=1994, type='Film', views=0),
    Film(title='Pulp Fiction3', year=1994, type='Film', views=0),
    Serial(title='The Simpsons1', year=1994, type='Serial', views=0, episode=17, season=3),
    Serial(title='The Simpsons2', year=1994, type='Serial', views=0, episode=11, season=3),
    Serial(title='The Simpsons3', year=1994, type='Serial', views=0, episode=12, season=3),
]
#3.
def generate_viwes():
    index = randint (0, len(library) -1)
    randItem = library[index]
    randItem.views = randint(0,100)
    return randItem

for i in range(10):
    generate_viwes()

#4.
# DD-MM-RRRR
print(f"Najpopularniejsze filmy i seriale z dnia {str(datetime.now().day).zfill(2)}.{str(datetime.now().month).zfill(2)}.{str(datetime.now().year).zfill(4)}")

#5.
def top_titles(count, content_type):
    sorted_library = sorted(library, key=lambda item: item.views, reverse=True)
    filter_by_type = list(filter(lambda item: (True if item.type == content_type else False) ,sorted_library))
    if count > len (filter_by_type):
        print ('Not enough items!')

    slice_library = filter_by_type[:count]
    return list (map(lambda item: item.title ,slice_library))
print(', '.join(top_titles(3, 'Film')))



# def filter_by_type(item):
#     return True if item.type == 'Film' else False

# filtered_items = filter(filter_by_type, library)

# def get_movies():
#     filtered_items = filter(lambda item: (True if item.type == 'Film' else False), library)
#     return list(filtered_items)

# def get_serials():
#     filtered_items = filter(lambda item: (True if item.type == 'Serial' else False), library)
#     return list(filtered_items)

# def search(phrase):
#     filtered_items = filter(lambda item: (True if phrase in item.title == phrase else False), library)
#     return list(filtered_items)

# library[3].play()
# library[0].play()

# print(get_movies())
# print(get_serials())
# print(search("Fiction1"))

# print(generate_viwes())
# print('---')

# for item in top_titles(2, 'Serial'):
#     print (item)
# print ('---')
# for item in library:
#     print(item)







