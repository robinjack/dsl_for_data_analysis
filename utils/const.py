import pandas as pd
import numpy as np


NUMERIC_DATATYPES = [np.int64, np.float64, np.bool, np.datetime64]

ORIGINATOR_TYPES = {'data': 'DataOriginator',
                    'function': 'FunctionOriginator'}

GRAMMAR_FILE_PATH = 'dsl/analysis_flow.tx'

CLASSNAMES = ['Program',
            'Statement',
            'Data',
            'Assignment',
            'Expression',
            'ArithmeticExpression',
            'BooleanExpression',
            'BooleanTerm',
            'NotFactor',
            'BooleanFactor',
            'BooleanLiteral',
            'Relation',
            'Additive',
            'ExpProduct',
            'ExpValue',
            'Value',
            'FunctionCall',
            'Function',
            'Sum',
            'Product',
            'Parameter',
            'Analysis',
            'Manipulation',
            'Train',
            'Test',
            'Score',
            'KeywordParameter',
            'Parameter',
              'PowValue'
               ]

