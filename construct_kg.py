import pandas as pd

entity_list = list({'movieid', 'rating', 'director', 'year',
                    'production', 'stars', 'genres'})

relation_list = list({'rating', 'director', 'year',
                      'production', 'stars', 'genres'})


def splitProduction(entity_set):
    production_list = list()
    for item in entity_set:
        item_list = item.replace('[', '').replace(
            ']', '').replace('\'', '').replace('\"', '').split(',')

        item_list = map(lambda i: i.lstrip(), item_list)
        production_list.append(item_list)

    return production_list


def splitGenres(entity_set):
    genres_list = list()
    for item in entity_set:
        item_list = item.split(' ')
        item_list = map(lambda i: i.lstrip(), item_list)
        genres_list.append(item_list)
    return genres_list


def splitStars(entity_set):
    star_list = list()
    for item in entity_set:
        item_list = str(item).split(',')
        item_list = map(lambda i: i.lstrip(), item_list)
        star_list.append(item_list)

    return star_list


def construct_kg(entity_dict):
    writer = open('kg.txt', 'w', encoding='utf-8')
    movie_set = entity_dict['movieid']

    for index, item in enumerate(movie_set):
        head = item
        for relation in relation_list:
            if(relation is 'production' or relation is 'genres' or relation is 'director' or relation is 'stars'):
                for tail in entity_dict[relation][index]:
                    writer.write('%s\t%s\t%s\n' %
                                 (head, 'film.'+relation, tail))
                    writer.write('%s\t%s\t%s\n' %
                                 (tail, relation+'.film', head))
            else:
                tail = entity_dict[relation][index]
                writer.write('%s\t%s\t%s\n' % (head, 'film.'+relation, tail))
                writer.write('%s\t%s\t%s\n' % (tail, relation+'.film', head))


movie_data = dict()
movie_data = pd.read_csv("all.csv", names=['movieid', 'title', 'imbdib', 'director',
                                           'rating', 'img_url', 'year', 'genres',
                                           'production', 'stars'], encoding='latin-1')
for item in entity_list:
    print(movie_data[item])


entity_dict = dict()

for item in entity_list:
    if(item is 'production'):
        entity_dict[item] = splitProduction(movie_data[item])
    elif(item is 'genres'):
        entity_dict[item] = splitGenres(movie_data[item])
    elif(item is 'stars' or item is 'director'):
        entity_dict[item] = splitStars(movie_data[item])
    else:
        entity_dict[item] = movie_data[item]


construct_kg(entity_dict)
