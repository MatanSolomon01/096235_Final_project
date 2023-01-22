import json
import pickle as pkl
from copy import deepcopy
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_jsn(path):
    with open(path) as f:
        file = json.load(f)
    return file


def dump_jsn(obj, path):
    with open(path, 'w') as f:
        json.dump(obj, f)


def list2dict(list):
    dict = {elm['id']: elm for elm in list}
    return dict


def list_of_dicts_to_list(listOdicts):
    list = []
    for dict in listOdicts:
        assert len(dict) == 1
        for value in dict.values():
            list.append(value)
    return list


def create_data():
    data_nutrition = load_jsn('data/raw/recipes_with_nutritional_info.json')
    data_nutrition = list2dict(data_nutrition)
    print("A")
    ids = data_nutrition.keys()
    assert len(set(ids)) == len(ids)
    raw_data = load_jsn('data/raw/Layers/layer1.json')
    print("B")
    raw_data = [rep for rep in raw_data if rep['id'] in ids]
    raw_data = list2dict(raw_data)
    assert len(ids) == len(raw_data)
    print("C")
    ingrid = load_jsn('data/raw/det_ingrs.json')
    ingrid = [rep for rep in ingrid if rep['id'] in ids]
    ingrid = list2dict(ingrid)
    print("D")
    data = {id_: {'ingredients_1': list_of_dicts_to_list(data_nutrition[id_]['ingredients']),
                  'instructions_1': list_of_dicts_to_list(data_nutrition[id_]['instructions']),
                  'nutr_per_ing_1': data_nutrition[id_]['nutr_values_per100g'],
                  'title_1': data_nutrition[id_]['title'],
                  'valid_2': ingrid[id_]['valid'],
                  'ingredients_2': list_of_dicts_to_list(ingrid[id_]['ingredients']),
                  'ingredients_3': list_of_dicts_to_list(raw_data[id_]['ingredients']),
                  'instructions_3': list_of_dicts_to_list(raw_data[id_]['instructions']),
                  } for id_ in ids}
    print("E")
    dump_jsn(data, 'data/data.json')


def transfer_to_df():
    data = load_jsn('data/data.json')
    data2 = {k: v for k, v in data.items() if all(v['valid_2'])}

    def del_valid_2(d):
        del d['valid_2']
        return d

    data3 = {k: del_valid_2(v) for k, v in data2.items()}
    data4 = deepcopy(data3)
    for v in data4.values():
        v.update(v['nutr_per_ing_1'])
        del v['nutr_per_ing_1']
    data_df = pd.DataFrame.from_dict(data4, orient='index')
    data_df = data_df[
        ['title_1', 'ingredients_1', 'ingredients_2', 'ingredients_3', 'instructions_1', 'instructions_3', 'energy',
         'fat', 'protein', 'salt', 'saturates', 'sugars']]
    pkl.dump(data_df, open('data/data_df.pkl', 'wb'))


create_data()
transfer_to_df()
