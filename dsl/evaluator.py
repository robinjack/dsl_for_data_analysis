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

    def update_model(self, model):
        self.model = model



if __name__ == "__main__":
    meta = metamodel_from_file('dsl/analysis_flow.tx')
    meta.register_obj_processors(OBJ_PROCESSORS)
    # model = meta.model_from_file('examples/simple_manipulation.analysis')
    model = meta.model_from_str("""
    LOAD data  "examples/iris.csv"
    MANIPULATION SELECT
        1 = 1 and 5 or 10^2 = 1 < 6 and 1 = 0 as bool1,
        1 = 1 as bool2
        FROM data; -> data2
    end
    """)
    result = Evaluator(model)
    result.evaluate()

