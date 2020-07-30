

"""
Output of REPL:
1. takes string as input
2. Evaluates it as an example of the analysis flow
3. Replaces the model 
4. Evaluates from the most recent statement
5. Adds the current state of the evaluator to a list
"""

from textx import metamodel_from_file
from dsl.evaluator import Evaluator
from semantic_model.memento import *
from dsl.analysis_flow_processor import OBJ_PROCESSORS

def revert(caretaker):
    id_to_load = input()
    try:
        int_id_to_load = int(id_to_load)
        caretaker.load(int_id_to_load)
        return
    except Exception as e:
        print(e)
        print("Try a different id.")
        revert(caretaker)

def repl(params=None):
    """
    This function runs the repl of the analysis flow.

    It instantiates the evaluator, the originator
    and the caretaker. It l

    It loads
    :return:
    """
    meta = metamodel_from_file('dsl/analysis_flow.tx')
    meta.register_obj_processors(OBJ_PROCESSORS)
    statement=""

    evaluator = Evaluator()
    originator = EvaluatorOriginator(evaluator)
    caretaker = Caretaker(originator)


    while True:
        new_statement = input()
        if new_statement == "inspect":
            caretaker.show_history()
        elif new_statement == 'revert':
            revert(caretaker)
        elif new_statement != 'end':
            try:
                statement_to_run = statement + "\n " + new_statement
                statement_model = meta.model_from_str(statement_to_run + "     end")
                statement = statement_to_run
                evaluator.update_model(statement_model)
                evaluator.evaluate()
                originator.set_state(evaluator, new_statement)
                caretaker.backup()
            except Exception as e:
                print(e)
                print("Invalid syntax or error in execution.")


        else:
            break




if __name__ == "__main__":
    repl()

