from dsl.evaluator import *
from semantic_model.data import Data
from dsl.analysis_flow_processor import OBJ_PROCESSORS



"""
There are two types of test in this test suite.

First is the functionality tests - can we do all of the 
functions that are exposed by the language - i.e. 
loading, analysing, manipulating, training, testing, reviewing.

Second is the analysis flow

"""

##############################
# Constants for testing
##############################

meta = metamodel_from_file('dsl/analysis_flow.tx')
meta.register_obj_processors(OBJ_PROCESSORS)
start_string = """ LOAD data "examples/iris.csv" """
end_string = """ end """
test_data = Data('examples/iris.csv')

def c(string_for_testing):
    """In order to minimise verbosity, I am adding a
    wrapper around the function meta.model_from_string.
    This means we can test the functionaality we want
    to test, without having to write out the LOAD / end
    sections of the code
    """
    return meta.model_from_str(start_string + string_for_testing + end_string)

def e(evaluator, string_to_get_from_symbol_table):
    """
    When we evaluate the end state of a program, we
    want to be able to get the string simply
    :param string_to_get_from_symbol_table:
    :return:
    """
    return evaluator.symbol_table[string_to_get_from_symbol_table]





    



##########################################################################
# Section one - testing functionality and expressions
##########################################################################

def test_load():
    model = meta.model_from_file('examples/test_load.analysis')
    result = Evaluator(model).evaluate()
    assert 'data' in result.symbol_table.keys()
    assert type(result.symbol_table['data']) == Data


def test_assignment():
    model = meta.model_from_file('examples/test_assignment.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert 'x' in result.symbol_table.keys()
    assert 1 in result.symbol_table.values()
#
#
def test_basic_arithmetic_expression():
    model = meta.model_from_file('examples/test_ae.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result.symbol_table['x'] == 2
#
#
def test_basic_sum_and_product_expression():
    model = meta.model_from_file('examples/test_ae2.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result.symbol_table['f'] == 17
#
#
def test_arithmetic_expression():
    model = meta.model_from_file('examples/test_arithmetic_expression.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result.symbol_table["z"] == 1
    assert result.symbol_table["e"] == 2
    assert result.symbol_table["f"] == 3
    assert result.symbol_table["o"] == 3.06
    assert result.symbol_table["u"] == 150
    assert result.symbol_table["x"] == 100


# def test_boolean_expression():
#     pass
#
# def test_multiple_boolean_expressions():
#     pass


# def test_order_of_operations():
#     model = meta.model_from_file('examples/test_order_of_operations.analysis')
#     result = Evaluator(model)
#     result.evaluate()
#     assert result.symbol_table["n"] == 51



#
# #####################################
# # Section two - analysis tests
# #####################################
#
def test_analysis_no_param_print():
    model = c(
        """
        ANALYSIS data print
        """
    )
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_analysis_print_specific_rows():
    model = c(
        """
        ANALYSIS data print start_row=15, end_row=20
        """
    )
    result = Evaluator(model)
    result.evaluate()
    assert result

def test_analysis_summarise_sum():
    model = c(
        """
        ANALYSIS data sum col=sepal_length
        """
    )
    result = Evaluator(model)
    result.evaluate()
    assert result
#
#
def test_analysis_summarise_mean():
    model = c(
        """
        ANALYSIS data mean col=sepal_length
        """
    )
    result = Evaluator(model)
    result.evaluate()
    assert result

#     TODO: add in tests for plotting
# def test_analysis_plot():
#     pass
#
#
def test_analysis_one_param():
    model = meta.model_from_file('examples/analysis_one_param.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result
#
#
def test_analysis_two_param():
    model = meta.model_from_file('examples/analysis_two_param.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result
#
#
# #####################################
# # Section three - manipulation tests
# #####################################
def test_manipulation_select():
    model = c("""
    MANIPULATION
    SELECT sepal_length as sepal_length1, sepal_length as sepal_length2 FROM data; -> new_data""")
    result = Evaluator(model)
    result.evaluate()
    assert len(set(result.symbol_table['new_data'].get_columns() + ['sepal_length1','sepal_length2'])) == len(set(['sepal_length1','sepal_length2']))

def test_manipulation_select_val():
    model = c("""MANIPULATION
    SELECT 1 as key FROM data; -> new_data""")
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_manipulation_select_val_plus_col():
    model = c("""MANIPULATION
    SELECT sepal_length + 1 as sepal_length FROM data;""")
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_manipulation_select_col_plus_col():
    model = c("""MANIPULATION
    SELECT sepal_length + sepal_length as sepal_length FROM data;""")
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_manipulation_select_star():
    model = c("""
    MANIPULATION SELECT * FROM data;
    """)
    result = Evaluator(model)
    result.evaluate()
    assert result
# #
# #
def test_manipulation_select_filter():
    model = c("""
    MANIPULATION
    SELECT sepal_length FROM data
    WHERE sepal_length < 3; -> sepal_data
    """)
    result = Evaluator(model)
    result.evaluate()
    assert result
#
#
def test_function_call_in_manipulation():
    model = c("""
        MANIPULATION
        SELECT log(1) as log_sepal_length
        from data; -> logged_data
        """)
    result = Evaluator(model)
    result.evaluate()
    assert e(result, 'logged_data').get_columns() == ['log_sepal_length']
#
def test_function_call_expression_in_manipulation():
    model = c("""
        MANIPULATION
        SELECT log(sepal_length + 1) as log_sepal_length
        from data;
        """)
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_function_call_plus_expression_in_manipulation():
    model = c("""
        MANIPULATION
        SELECT log(sepal_length + 1) + 1 as log_sepal_length
        from data;
        """)
    result = Evaluator(model)
    result.evaluate()
    assert result
#
#
# def test_groupby_one_column():
#     model = meta.model_from_file('examples/groupby_one_column.analysis')
#     result = Evaluator(model)
#     result.evaluate()
#     assert result
#
#
# ###########################################################################
# # Section four - training + prep for training tests
# ###########################################################################
def test_simple_train():
    model = meta.model_from_file('examples/simple_train.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_simple_test():
    model = meta.model_from_file('examples/simple_test.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_simple_score():
    model = meta.model_from_file('examples/simple_score.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result
#
#
# #####################################
# # Section five - MVP tests
# #####################################
#
# """
# Thirdly, is the analysis workflow MVP files.
# These three tests will comprise the MVP of the product.
# There are three basic tests:
# 1. The most basic analysis possible (look at the data, choose Y, and predict)
# 2. The most basic manipulation possible
#     look at the data
#     choose Y
#     predict Y
#     review results
#     manipulate the data (SELECT col + 1 where col < 10)
#     predict Y
#     compare results
# 3. Two manipulations + rewind a manipulation to a previous snapshot
#     Same as above, but with two manipulations done,
#     Inspect the results + compare them
# """
def test_simple_program():
    model = meta.model_from_file('examples/test_program.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_simple_manipulation():
    model = c("""
print(data)
s = 1
MANIPULATION SELECT *, sepal_length + 1 as target
FROM data WHERE sepal_length + 1 > 3; -> new_data
TRAIN new_data target=target
TEST new_data target=target
SCORE new_data
    """)

    result = Evaluator(model)
    result.evaluate()
    assert result
#
def test_two_manipulations_and_rewind():
    model = meta.model_from_file('examples/two_manipulations.analysis')
    result = Evaluator(model)
    result.evaluate()
    assert result





