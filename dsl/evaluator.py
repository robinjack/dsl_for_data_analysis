from textx import metamodel_from_file
from semantic_model.data import Data
import numpy as np
from dsl.symbol_table import SYMBOL_TABLE



class Evaluator:

    """
    The evaluator class evaluates the semantic model generated
    by the analysis flow.

    It accepts a model, and then iterates over the "statements",
    evaluating each one as it goes.


    """
    def __init__(self, model=None):
        self.symbol_table = SYMBOL_TABLE
        self.function_table = {
            'analysis_flow.Data': self.load,
            'analysis_flow.Assignment': self.assignment,
            'analysis_flow.Expression': self.expression,
            'analysis_flow.ArithmeticExpression': self.arithmetic_expression,
            'analysis_flow.Value': self.value,
            'analysis_flow.FunctionCall': self.function_call,
            'analysis_flow.Function': self.function_call,
            'analysis_flow.Sum': self.arithmetic_expression,
            'analysis_flow.Product': self.arithmetic_expression,
            'analysis_flow.Parameter': self.parameter,
        }
        self.model = model
        self.index=0

    def run(self):
        for statement in self.model.statement[self.index:]:
            self.evaluate(statement)
            self.index += 1
        return self

    def evaluate(self, statement):
        """
        There are a few forms that evaluate can take:
        1. a TextX class, in which case look up the appropriate function
        to deal with this class in the function table, and deal with it appropriately

        2. An id for the symbol table - in which case look it up in the symbol table
        and return the value
        3. a value  - in which caase return the value

        I could make this more succinct by using self.symbol_table.get(statement, statement)
        but this is less legible.
        :param statement:
        :return:
        """
        if type(statement) == list:
            return (self.evaluate(s) for s in statement)

        elif hasattr(statement, '_tx_fqn'):
            return self.function_table[statement._tx_fqn](statement)
        elif statement in self.symbol_table:
            return self.symbol_table[statement]
        else:
            return statement

    def load(self, statement):
        """
        The load function not only loads the data, it also
        adds all of the columns as global variables to be
        used as the analyst likes.
        TODO: add the code to add in the global variables.
        :param statement:
        :return:
        """
        if statement.name in self.symbol_table.keys():
            return self.symbol_table[statement.name]
        else:
            data = Data(statement.fp)
            self.symbol_table[statement.name] = data
            return data


    def assignment(self, statement):
        """
        The assignment statement adds the key to the symbol table,
        and evaluates the right side of the assignment
        :param statement:
        :return:
        """
        self.symbol_table[statement.key] = self.evaluate(statement.value)

    def expression(self, statement):
        """
        The expression function does not currently do anything,
        as it is an abstract grammatical rule, so it will
        never be instantiated.

        :param statement:
        :return:
        """
        return

    def arithmetic_expression(self, statement):
        """
        The arithmetic expression function
        If there are no operators, it just evaluates the operand.

        If there are operators, it pops the statement's first
        operator and first operand from the statement and evaluates them.
        It then pass the operand to the left side of the operator,
        and evaluates the rest of the statement and passes it to the right"""

        if len(statement.operator) == 0:
            return self.evaluate(statement.op.pop())
        else:
            operator = statement.operator.pop()
            operand = statement.op.pop()
            return self.evaluate(operator)(
                self.evaluate(operand),
                self.evaluate(statement))


    def value(self, statement):
        """
        If the object is a Value then it just returns
        the operand value
        :param statement:
        :return:
        """

        return statement.op

    def function_call(self, statement):
        """If the class is a function call, you evaluate
        the function call, and then apply it to the evaluated
         expression that was passed to it.

         By doing this, we are passing by value, as we evaluate
         the parameters before we pass them to the function."""
        return self.evaluate(statement.functionName)(
            *self.evaluate(statement.exp))

    def parameter(self, statement):
        return self.evaluate(statement.value)

    def update_model(self, model):
        self.model=model


if __name__ == "__main__":

    meta = metamodel_from_file('dsl/analysis_flow.tx')
    model = meta.model_from_file('examples/test_program.analysis')
    result = Evaluator(model)
    result.run()

