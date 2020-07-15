from dsl.evaluator import *
from semantic_model.data import Data


meta = metamodel_from_file('dsl/analysis_flow.tx')


# TODO: test evaluate
# def evaluate(self, command):
#     return self.function_table[command._tx_fqn](command)


def test_load():
    model = meta.model_from_file('examples/test_load.analysis')
    result = Evaluator(model).run()
    assert 'data' in result.symbol_table.keys()
    assert type(result.symbol_table['data']) == Data

def test_assignment():
    model = meta.model_from_file('examples/test_assignment.analysis')
    result = Evaluator(model)
    result.run()
    assert 'x' in result.symbol_table.keys()
    assert 1 in result.symbol_table.values()

def test_basic_arithmetic_expression():
    model = meta.model_from_file('examples/test_ae.analysis')
    result = Evaluator(model)
    result.run()
    assert result.symbol_table['x'] == 2

def test_basic_sum_and_product_expression():
    model = meta.model_from_file('examples/test_ae2.analysis')
    result = Evaluator(model)
    result.run()
    assert result.symbol_table['f'] == 17


# def test_arithmetic_expression():
#     model = meta.model_from_file('examples/test_arithmetic_expression.analysis')
#     result = Evaluator(model)
#     result.run()
#     assert result.symbol_table["z"] == 1
#     assert result.symbol_table["e"] == 2
#     assert result.symbol_table["f"] == 3
#     assert result.symbol_table["o"] == 2.06
#     assert result.symbol_table["x"] == 101
#     assert result.symbol_table["y"] == 100101

"""

def test_function_call():
    model = meta.model_from_file('examples/test_function_call.analysis')
    result = Evaluator(model)
    assert False
    
    """


def test_simple_program():
    model = meta.model_from_file('examples/test_program.analysis')
    result = Evaluator(model)
    result.run()





