from textx import metamodel_from_file
from semantic_model.data import Data




class Evaluator:

    def __init__(self, model):
        self.symbol_table = {}
        self.function_table = {
            'analysis_flow.Data': self.load,
            'analysis_flow.Assignment': self.assignment,
            'analysis_flow.Expression': self.expression,
            'analysis_flow.ArithmeticExpression': self.arithmetic_expression,
            'analysis_flow.Operator': self.operator,
            'analysis_flow.Value': self.value,
            'analysis_flow.FunctionCall': self.function_call,
            'analysis_flow.Function': self.function
        }
        self.model=model

    def run(self):
        for statement in self.model.statement:
            self.evaluate(statement)
        return self

    def evaluate(self, statement):
        if hasattr(statement, '_tx_fqn'):
            return self.function_table[statement._tx_fqn](statement)
        else:
            return statement

    def load(self, statement):
        data = Data(statement.fp)
        self.symbol_table[statement.name] = data

    def assignment(self, statement):
        self.symbol_table[statement.key] = self.evaluate(statement.value)

    def expression(self, statement):
        return

    def arithmetic_expression(self, statement):
        return

    def operator(self, statement):
        return

    def value(self, statement):
        return

    def function_call(self, statement):
        return

    def function(self, statement):
        return

meta = metamodel_from_file('dsl/analysis_flow.tx')
model = meta.model_from_file('examples/test_ae.analysis')
# d = Data('examples/iris.csv')
#
# d.set_target('sepal_length')
