from semantic_model.data import Data
import numpy as np
from utils.function_utils import cartesian_product,  \
    return_item_or_remove_from_list
from utils.const import *
from utils.function_utils import *
from collections import ChainMap
from itertools import accumulate
from utils.plots import *


"""

"""


def program(self, symbol_table):
    for statement in self.statement[symbol_table['index']:]:
        statement.evaluate(statement, symbol_table)
        symbol_table['index'] += 1
    return self


def load(self, symbol_table):
    """
    The load function not only loads the data, it also
    adds all of the columns as global variables to be
    used as the analyst likes.
    TODO: add the code to add in the global variables.
    :param symbol_table, statement:
    :return:
    """
    if self.name in symbol_table.keys():
        return symbol_table[self.name]
    else:
        data = Data(self.fp)
        symbol_table[self.name] = data
        return data




def assignment(self, symbol_table):
    """
    The assignment statement adds the key to the symbol table,
    and evaluates the right side of the assignment
    :param self, symbol_table:
    :return:
    """
    symbol_table[self.key] = self.value.evaluate(self.value, symbol_table)


def expression(self):
    """
    The expression function does not currently do anything,
    as it is an abstract grammatical rule, so it will
    never be instantiated.

    :param statement:
    :return:
    """
    return


def arithmetic_expression(self, symbol_table):
    """
    The arithmetic expression function
    If there are no operators, it just evaluates the operand.

    If there are operators, it pops the statement's first
    operator and first operand from the statement and evaluates them.
    It then pass the operand to the left side of the operator,
    and evaluates the rest of the statement and passes it to the right"""
    if not hasattr(self, 'operator') and hasattr(self.op, '_tx_fqn'):
        return self.op.evaluate(self.op, symbol_table)
    if not hasattr(self, 'operator'):
        return self.op
    if len(self.operator) == 0:
        operand =self.op.pop(0)
        return operand.evaluate(operand, symbol_table)
    else:
        operator = self.operator.pop(0)
        op = self.op.pop(0)
        operand = op.evaluate(op, symbol_table)
        return symbol_table[operator](
            operand,
            self.evaluate(self, symbol_table)
            )


def value(self, symbol_table):
    """
    If the object is a Value then it just returns
    the operand value
    :param statement:
    :return:

    TODO: figure out if this implementation hides bugs
    """
    if symbol_table.get(self.op):
        return symbol_table.get(self.op)
    if type(self.op) == str:
        d = symbol_table[CURRENT_QUERY_DATASET]
        if self.op in d.get_columns():
            return pd.DataFrame(d.get_column(self.op), columns=[self.op])
    if hasattr(self.op, '_tx_fqn'):
        return self.op.evaluate(self.op, symbol_table)
    else:
        return self.op


def function_call(self, symbol_table):
    """If the class is a function call, you evaluate
    the function call, and then apply it to the evaluated
     expression that was passed to it.

     By doing this, we are passing by value, as we evaluate
     the parameters before we pass them to the function."""
    function = self.functionName.evaluate(
        self.functionName, symbol_table) \
        if hasattr(self.functionName,'_tx_fqn') \
        else symbol_table[self.functionName]

    args = [exp.evaluate(exp, symbol_table) \
                if hasattr(exp, '_tx_fqn') \
        else exp for exp in self.exp]

    return function(*args)


def analysis(self, symbol_table):
    try:
        data = symbol_table[self.data]
    except KeyError as e:
        print(e, " Value not found in symbol table.")
    function=symbol_table[self.functionName]
    args = dict(ChainMap(*[(arg.evaluate(arg)) for arg in self.args]))
    args['data'] = data
    result = function(**args)
    if hasattr(self, 'result'):
        symbol_table[self.result] = result
    return result


def manipulation(self, symbol_table):
    query_result = self.query.evaluate(self.query, symbol_table)
    if 'name' != "":
        symbol_table[self.name] = Data(query_result)
    return query_result


def query(self, symbol_table):
    """
    This query applies the classic formulation, split, apply,
    combine.
    Split + Combine are done if there is a groupby clause.
    There are several parts to the query:
    1. maps (select parts)
    2. from_items (the dataframes we're querying)
    3. filters (where clause)
    4. groups (anything we're grouping by)
    5. having (filters post grouping/aggregation)

    The or
    :param self:
    :param symbol_table:
    :return:
    """
    dataset = cartesian_product([symbol_table[data] for data in self.from_items])
    maps = self.maps if self.maps else []
    groups=self.groups if self.groups else []
    # having=self.having
    symbol_table[CURRENT_QUERY_DATASET] = dataset
    # need to instantiate this variable here so we can
    # treat grouped queries + non-grouped queries similarly
    grouped_dataset=dataset

    # Note:
    # Due to issues with how we have implemented this,
    # we will skip grouping by expressions for now
    # SPLIT
    if self.groups:
        grouped_dataset = dataset.data.groupby(groups)

    """
    we have groups
    1. for each group, obtain a dataframe from the original groups +
    the group
    2. then, apply the aggregation function to the remaining maps
    3. join the original grouped rows to the result
    4. append the results to each other

    """

    # APPLY

    symbol_table[CURRENT_QUERY_MAPS] = [m for m in maps if m not in groups]
    symbol_table[CURRENT_QUERY_GROUPS] = groups
    symbol_table[CURRENT_QUERY_FILTERS] = self.filters

    # COMBINE
    if hasattr(grouped_dataset, 'groups'):
        try:
            combined_output = []
            for group in grouped_dataset.groups:
                symbol_table[CURRENT_QUERY_DATASET] = Data(grouped_dataset._selected_obj.iloc[grouped_dataset.groups[group].values,])
                mapped_group = apply(symbol_table)
                combined_output.append(mapped_group)
            dataset = pd.concat(combined_output)
        except Exception as e:
            print("Exception found: ", e, """\n Group by not implemented yet due to
             side effects of evaluating the expression (current design expects
             to only be evaluated once). This presents a significant
             blocker to implementing group by.  
             """)
    else:
        dataset = apply(symbol_table)


    return dataset

def columnExpression(self, symbol_table):
    """
    This expression returns a mapped column,
    or list of mapped columns.

    Case 1: the column is specified, but no op. We return the column
    Case 2: the column name is specified using AS, but it is
    the results of an expression. We add a new column to the
    data frame, with the name of the column. This can also override existing columns.
    Case 3: We are passed "*". In this instance we pass back all of the
    columns.


    :param self:
    :param symbol_table:
    :return:
    """
    if self.colname == SELECT_ALL_OPERATOR:
        return symbol_table[CURRENT_QUERY_DATASET].data

    elif self.op is None:
        # We treat this as either being a column call, or a select *
        # try:
        return symbol_table[CURRENT_QUERY_DATASET].get_column(self.colname)
        # except Exception as e:
        #     print("Thrown Exception due to invalid column selected:", e)


    else:
        symbol_table[CURRENT_QUERY_DATASET].set_column(self.colname, self.op.evaluate(self.op, symbol_table))
        return symbol_table[CURRENT_QUERY_DATASET].get_column(self.colname)
        # return pd.DataFrame(self.op.evaluate(self.op, symbol_table), columns=[self.colname])


def analysis_print(data=None, start_row=0, end_row=5, column=None):
    if column:
        print(data.get_column(column)[start_row, end_row])
    else:
        print(data.view(start_row, end_row))


def analysis_mean(data, col=None):
    if col == None:
        return data.data.mean()
    else:
        return np.mean(data.get_column(col))

def analysis_sum(data, col=None):
    if col==None:
        return data.sum()
    else:
        return data.get_column(col).sum()


def analysis_count(data, col=None):
    if col==None:
        return data.count()
    else:
        return data.get_column(col).count()

def analysis_percentile(data, col, ntile=0.5):
    try:
        return data.get_column(col).quantile(ntile)
    except KeyError as e:
        print(e, f" '{col}' column does not exist")


def analysis_plot(data, plot_type='pairs', **kwargs):
    params = {key: value for key, value in kwargs}
    params['data'] = data
    plot = KIND_TO_PLOT_FUNC_DICT[plot_type](**params)
    plt.show()
    return plot


def keywordParameter(self):
    return {self.param: self.value.evaluate(self.value)}


def parameter(self):
    if hasattr(self.value, '_tx_fqn'):
        return self.value.evaluate()
    else:
        return self.value


def update_model(self, model):
    self.model = model


def train(self, symbol_table):
    args = dict(ChainMap(*[(arg.evaluate(arg)) for arg in self.parameters]))
    data = symbol_table[self.data]
    data.set_target(args['target'])
    return data.train()


def test(self, symbol_table):
    args = dict(ChainMap(*[(arg.evaluate(arg)) for arg in self.parameters]))
    data = symbol_table[self.data]
    # data.set_target(args['target'])
    return data.test()


def score(self, symbol_table):
    score = symbol_table[self.data].score()
    print("Score: ", score)
    return score


FUNCTION_TABLE = {
            'analysis_flow.Program': program,
            'analysis_flow.Data': load,
            'analysis_flow.Assignment': assignment,
            'analysis_flow.Expression': expression,
            'analysis_flow.ArithmeticExpression': arithmetic_expression,
            'analysis_flow.Value': value,
            'analysis_flow.FunctionCall': function_call,
            'analysis_flow.Function': function_call,
            'analysis_flow.Sum': arithmetic_expression,
            'analysis_flow.Product': arithmetic_expression,
            'analysis_flow.Parameter': parameter,
            'analysis_flow.Analysis': analysis,
            'analysis_flow.AnalysisFunction': function_call,
            'analysis_flow.Manipulation': manipulation,
            'analysis_flow.Train': train,
            'analysis_flow.Test': test,
            'analysis_flow.Score': score,
            'analysis_flow.PowValue': arithmetic_expression,
            'analysis_flow.ExpValue': value,
            'analysis_flow.ExpProduct': arithmetic_expression,
            'analysis_flow.ExpPower': arithmetic_expression,
            'analysis_flow.Additive': arithmetic_expression,
            'analysis_flow.Relation': arithmetic_expression,
            'analysis_flow.BooleanTerm': arithmetic_expression,
            'analysis_flow.BooleanExpression': arithmetic_expression,
            'analysis_flow.BoolExp': arithmetic_expression,
            'analysis_flow.Select': query,
            'analysis_flow.ColExp': columnExpression,
            'analysis_flow.KeywordParameter': keywordParameter,
            'analysis_flow.Print': analysis_print,
            'analysis_flow.Mean': analysis_mean,
            'analysis_flow.Sum': analysis_sum,
            'analysis_flow.Count': analysis_count,
            'analysis_flow.Percentile': analysis_percentile,
            'analysis_flow.Plot': analysis_plot,

                }

