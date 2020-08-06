import numpy as np
from dsl.function_table import *


"""Current reserved words for the manipulation:
    print
    log
    mean
    sum
    percentile
    count
    train
    test
    target
    results
"""

SYMBOL_TABLE = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: np.power(x, y),
    '%': lambda x, y: x % y,
    'print': analysis_print,
    'log': lambda x: np.log(x),
    'mean': analysis_mean,
    'sum': analysis_sum,
    'percentile':analysis_percentile,
    'count': np.count_nonzero,
    'train': lambda x: x.train(),
    'test': lambda x: x.test(),
    'target': lambda data, col: data.set_target(col),
    'results': lambda data: print(data.score()),
    '=' : lambda x, y: x == y,
    "<": lambda x,y : x < y,
    ">": lambda x,y : x > y,
    "!=": lambda x,y: x != y,
    "and": lambda x,y: x and y,
    "or": lambda x,y: x or y,
    'plot' : analysis_plot
}



