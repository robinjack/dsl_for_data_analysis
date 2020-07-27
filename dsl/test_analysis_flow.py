"""
This series of tests loads a model.

We can then see if the syntax works.\



"""

from dsl.evaluator import *
from semantic_model.data import Data

meta = metamodel_from_file('dsl/analysis_flow.tx')


#####################################
# Section one - testing basic syntax
#####################################

def test_load():
    assert meta.model_from_file('examples/test_load.analysis')


def test_assignment():
    assert meta.model_from_file('examples/test_assignment.analysis')


def test_basic_arithmetic_expression():
    assert meta.model_from_file('examples/test_ae.analysis')


def test_basic_sum_and_product_expression():
    assert meta.model_from_file('examples/test_ae2.analysis')

# def test_arithmetic_expression():
#     assert meta.model_from_file('examples/test_arithmetic_expression.analysis')


#####################################
# Section two - flow syntax tests
#####################################

def test_analysis_no_param():
    assert meta.model_from_file('examples/analysis_one_param.analysis')


def test_analysis_one_param():
    assert meta.model_from_file('examples/analysis_one_param.analysis')


def test_analysis_two_param():
    assert meta.model_from_file('examples/analysis_two_param.analysis')


def test_manipulation_select():
    assert meta.model_from_file('examples/basic_manipulation_select.analysis')


def test_manipulation_select_map():
    assert meta.model_from_file('examples/basic_manipulation_select_map.analysis')


def test_manipulation_select_filter():
    assert meta.model_from_file('examples/basic_manipulation_select_filter.analysis')


def test_function_call_in_manipulation():
    assert meta.model_from_file('examples/function_call_in_manipulation.analysis')

def test_groupby_one_column():
    assert meta.model_from_file('examples/groupby_one_column.analysis')


def test_simple_train():
    assert meta.model_from_file('examples/simple_train.analysis')

def test_simple_test():
    assert meta.model_from_file('examples/simple_test.analysis')

def test_simple_score():
    assert meta.model_from_file('examples/simple_score.analysis')


#####################################
# Section three - MVP syntax tests
#####################################

def test_simple_program():
    assert meta.model_from_file('examples/test_program.analysis')

def test_simple_manipulation_flow():
    assert meta.model_from_file('examples/simple_manipulation.analysis')

def test_two_manipulations_and_rewind():
    assert meta.model_from_file('examples/two_manipulations_and_rewind.analysis')





if __name__ == "__main__":
    meta = metamodel_from_file('analysis_flow.tx')
    meta.model_from_file('examples/test_load.analysis')