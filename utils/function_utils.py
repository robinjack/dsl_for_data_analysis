import pandas as df



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

