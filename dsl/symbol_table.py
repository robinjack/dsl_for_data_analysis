import numpy as np


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
    'print': lambda x: print(x),
    'log': lambda x: x.log(),
    'mean': lambda x: x.mean,
    'sum': lambda x: x.sum(),
    'percentile': lambda x, y: np.percentile(x, y),
    'count': np.count_nonzero,
    'train': lambda x: x.train(),
    'test': lambda x: x.test(),
    'target': lambda data, col: data.set_target(col),
    'results': lambda data: print(data.score())

}



