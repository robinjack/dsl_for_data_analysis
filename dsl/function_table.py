from semantic_model.data import Data
import numpy as np

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
    # if not hasattr(self, 'operator'):
    #     return self.op.evaluate(self, symbol_table)
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
        for d in symbol_table['current_query_datasets']:
            if self.op in d.get_columns():
                return d.data[self.op]
    if hasattr(self.op, '_tx_fqn'):
        return self.op.evaluate(self.op, symbol_table)
    else:
        return self.op


def function_call(self):
    """If the class is a function call, you evaluate
    the function call, and then apply it to the evaluated
     expression that was passed to it.

     By doing this, we are passing by value, as we evaluate
     the parameters before we pass them to the function."""
    return self.functionName.evaluate()(
        *self.exp.evaluate())


def analysis(self, symbol_table):
    data = self.data.evaluate()
    function = self.functionName.evaluate()
    args = {arg.param: arg.value for arg in self.args}
    args['data'] = data
    return function(*args)


def manipulation(self, symbol_table):
    return self.query.evaluate(self.query, symbol_table)


def query(self, symbol_table):
    """
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
    datasets = self.from_items
    maps = self.maps
    filters=self.filters
    # groups=self.groups
    having=self.having

    symbol_table['current_query_dataset'] = datasets
    for map in maps:
        map.evaluate(map, symbol_table)
    for filter in filters:
        filter.evaluate(filter, symbol_table)

    return


def parameter(self):
    return self.value.evaluate()


def update_model(self, model):
    self.model = model


def train(self):
    return self.data.evaluate().train()


def test(self):
    return self.data.evaluate().test()


def score(self):
    self.data.evaluate().score()


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
            'analysis_flow.Manipulation': manipulation,
            'analysis_flow.Train': train,
            'analysis_flow.Test': test,
            'analysis_flow.Score': score,
            'analysis_flow.PowValue': arithmetic_expression}

