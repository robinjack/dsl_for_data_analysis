import pandas as pd
from utils.const import *
from copy import copy



def cartesian_product(dfs):
    if len(dfs) == 0:
        return
    if len(dfs) == 1:
        return dfs.pop()
    else:
        df = dfs.pop()
        return df.assign(key=1).merge(
            cartesian_product(dfs).assign(key=1), on="key").drop(
            "key", axis=1)


def return_item_or_remove_from_list(item):
    return item.pop() if type(item) == list else item


def unpack(l):
    if l == []:
        return []
    if type(l) != list:
        return [l]
    else:
        return unpack(l[0]) + unpack(l[1:])


def concat_without_duplicates(df_list):
    try:
        initial_df = df_list.pop()
    except IndexError as e:
        print("Tried to concat without any items.")

    if len(df_list)==0:
        return initial_df
    else:
        while len(df_list) > 0:
            second_df = df_list.pop()
            second_df_columns = second_df.columns if type(second_df)==pd.DataFrame \
                else second_df.name
            second_df = second_df[[set(second_df_columns) - set(initial_df.columns) ]]
            initial_df = pd.concat([initial_df, second_df], axis=1)

    return initial_df


# https://jakevdp.github.io/blog/2017/03/22/group-by-from-scratch/
"""
Need to apply the SPLIT-APPLY-COMBINE pattern
in order to do group by 
"""

def split(self, symbol_table):
    pass

def apply(symbol_table):
    maps = copy(symbol_table[CURRENT_QUERY_MAPS])
    data = [map.evaluate(map, symbol_table) for map in
            maps]

    dataset = pd.concat(data, axis=1)
    dataset = dataset.loc[:, ~dataset.columns.duplicated()]

    if symbol_table[CURRENT_QUERY_FILTERS]:
        f = return_item_or_remove_from_list(symbol_table[CURRENT_QUERY_FILTERS])
        f.evaluate(f, symbol_table)

    return dataset

def combine():
    pass


# In order to use apply multiple times, I need a function that can copy TextX objects


