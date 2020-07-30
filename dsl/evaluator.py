from textx import metamodel_from_file
from dsl.symbol_table import SYMBOL_TABLE
from dsl.function_table import FUNCTION_TABLE
from dsl.analysis_flow_processor import OBJ_PROCESSORS



class Evaluator:

    """
    The evaluator class evaluates the semantic model generated
    by the analysis flow.

    It accepts a model, and then iterates over the "statements",
    evaluating each one as it goes.

    The model assumes that it will receive only objects that
    have a .evaluate() method.



    """
    def __init__(self, model=None):
        self.symbol_table = SYMBOL_TABLE
        self.function_table = FUNCTION_TABLE
        self.model = model
        self.symbol_table['index']=0


    def evaluate(self):
        """
        This function assumes that each of its children has
        an "evaluate" function. It evaluates the model
        :param statement:
        :return:
        """
        self.model.evaluate(self.model, self.symbol_table)
        return self
        # if type(statement) == list:
        #     return (self.evaluate(s) for s in statement)
        #
        # elif hasattr(statement, '_tx_fqn'):
        #     return self.function_table[statement._tx_fqn](statement)
        # elif statement in self.symbol_table:
        #     return self.symbol_table[statement]
        # else:
        #     return statement

    def update_model(self, model):
        self.model = model



if __name__ == "__main__":
    meta = metamodel_from_file('dsl/analysis_flow.tx')
    meta.register_obj_processors(OBJ_PROCESSORS)
    model = meta.model_from_file('examples/test_order_of_operations.analysis')
    result = Evaluator(model)
    result.evaluate()

