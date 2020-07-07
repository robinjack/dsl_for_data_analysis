from textx import metamodel_from_file

simple_meta = metamodel_from_file('analysis_flow.tx')
from semantic_model.data import Data


example_simple_model = simple_meta.model_from_file('examples/simple_model.analysis')

print(example_simple_model)

class Evaluator:
    symbol_table = {}
    function_table = {}

    def __init__(self, model):
        for command in model.command:
            self.evaluate(command)

    def evaluate(self, command):
        return self.function_table[command._tx_fqn](command)

    def load(self, command):
        data = Data(command.fp)
        self.symbol_table[command.name] = data

    def assignment(self, command):
        self.symbol_table[command.key] = command.value

    def expression(self, command):
        return

    def arithmetic_expression(self, command):
        return

    def operator(self, command):
        return

    def value(self, command):
        return

    def function_call(self, command):
        return

    def function(self, command):
        return






d = Data(example_simple_model.data.fp)

for c in example_simple_model.command:
    print(c.data)


print(d)