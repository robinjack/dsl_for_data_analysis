from dsl.evaluator import *
from semantic_model.data import Data

meta = metamodel_from_file('dsl/analysis_flow.tx')

"""
There are two types of test in this test suite.

First is the functionality tests - can we do all of the 
functions that are exposed by the language - i.e. 
loading, analysing, manipulating, training, testing, reviewing.

Second is the analysis flow

"""

    



#####################################
# Section one - testing functionality
#####################################

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


def test_arithmetic_expression():
    model = meta.model_from_file('examples/test_arithmetic_expression.analysis')
    result = Evaluator(model)
    result.run()
    assert result.symbol_table["z"] == 1
    assert result.symbol_table["e"] == 2
    assert result.symbol_table["f"] == 3
    assert result.symbol_table["o"] == 2.06
    assert result.symbol_table["x"] == 101
    assert result.symbol_table["y"] == 100101

#####################################
# Section two - basic functionality tests
#####################################

def test_analysis_no_param():
    model = meta.model_from_file('examples/analysis_one_param.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_analysis_one_param():
    model = meta.model_from_file('examples/analysis_one_param.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_analysis_two_param():
    model = meta.model_from_file('examples/analysis_two_param.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_manipulation_select():
    model = meta.model_from_file('examples/basic_manipulation_select.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_manipulation_select_map():
    model = meta.model_from_file('examples/basic_manipulation_select_map.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_manipulation_select_filter():
    model = meta.model_from_file('examples/basic_manipulation_select_filter.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_function_call_in_manipulation():
    model = meta.model_from_file('examples/function_call_in_manipulation.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_groupby_one_column():
    model = meta.model_from_file('examples/groupby_one_column.analysis')
    result = Evaluator(model)
    result.run()
    assert result


def test_simple_train():
    model = meta.model_from_file('examples/simple_train.analysis')
    result = Evaluator(model)
    result.run()
    assert result

def test_simple_test():
    model = meta.model_from_file('examples/simple_test.analysis')
    result = Evaluator(model)
    result.run()
    assert result

def test_simple_score():
    model = meta.model_from_file('examples/simple_score.analysis')
    result = Evaluator(model)
    result.run()
    assert result


#####################################
# Section three - MVP tests
#####################################

"""
Thirdly, is the analysis workflow MVP files.
These three tests will comprise the MVP of the product.
There are three basic tests:
1. The most basic analysis possible (look at the data, choose Y, and predict)
2. The most basic manipulation possible 
    look at the data
    choose Y
    predict Y
    review results
    manipulate the data (SELECT col + 1 where col < 10)
    predict Y
    compare results
3. Two manipulations + rewind a manipulation to a previous snapshot
    Same as above, but with two manipulations done,
    Inspect the results + compare them
"""
def test_simple_program():
    model = meta.model_from_file('examples/test_program.analysis')
    result = Evaluator(model)
    result.run()
    assert result

def test_simple_manipulation():
    model = meta.model_from_file('examples/simple_manipulation.analysis')
    result = Evaluator(model)
    result.run()
    assert result

def test_two_manipulations_and_rewind():
    model = meta.model_from_file('examples/two_manipulations_and_rewind.analysis')
    result = Evaluator(model)
    result.run()
    assert result





