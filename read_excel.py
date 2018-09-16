import pandas as pd

entity_list = list({'movieid', 'rating', 'director', 'year',
                    'production', 'stars', 'genres'})

relation_list = list({'rating', 'director', 'year',
                      'production', 'stars', 'genres'})


def splitProduction(entity_set):
    entity_list = list()
    for item in entity_set:
        item_list = item.replace('[', '').replace(
            ']', '').replace('\'', '').replace('\"', '').split(',')

        for l_item in item_list:
            entity_list.append(l_item)

    entity_list = map(lambda i: i.lstrip(), entity_list)
    return set(entity_list)


def splitGenres(entity_set):
    entity_list = list()
    for item in entity_set:
        item_list = item.split(' ')
        for l_item in item_list:
            entity_list.append(l_item)

    entity_list = map(lambda i: i.lstrip(), entity_list)
    return set(entity_list)


def splitStars(entity_set):
    entity_list = list()
    for item in entity_set:
        item_list = str(item).split(',')
        for l_item in item_list:
            entity_list.append(l_item)

    entity_list = map(lambda i: i.lstrip(), entity_list)
    return set(entity_list)


if __name__ == '__main__':

    data = pd.read_csv("movieinfo/movies_1.csv")

    entity_dict = dict()

    for item in entity_list:
        if(item is 'production'):
            entity_dict[item] = splitProduction(set(data[item]))
        elif(item is 'genres'):
            entity_dict[item] = splitGenres(set(data[item]))
        elif(item is 'stars' or item is 'director'):
            entity_dict[item] = splitStars(set(data[item]))
        else:
            entity_dict[item] = set(data[item])

    entity2index = dict()

    entity = list()
    for item in entity_dict:
        entity.extend(entity_dict[item])

    for i, item in enumerate(entity):
        entity_dict[item] = i

    # 将entity2index写入文件中
    writer = open('entity2index.txt', 'w', encoding='utf-8')
    for i, item in enumerate(entity):
        writer.write('%s\t%d\n' % (item, i))
    writer.close()
