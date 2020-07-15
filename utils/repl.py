"""
Test REPL 1L:
from code import InteractiveConsole

header="Welcome to this REPL"
footer = "this will be joyful"

scope_vars = {"test": 42}

InteractiveConsole(locals=scope_vars).interact(header, footer)"""

"""
Output of REPL:
1. takes string as input
2. Evaluates it as an example of the analysis flow
3. Replaces the model 
4. Evaluates from the most recent statement
"""

from textx import metamodel_from_file
from dsl.evaluator import Evaluator




meta = metamodel_from_file('dsl/analysis_flow.tx')
statement=""

evaluator = Evaluator()

while True:
    statement += input()
    if statement != 'end':
        try:
            statement_model = meta.model_from_str(statement + "     end")
        except Exception as e:
            print(e)
            print("Invalid syntax or error in execution.")

        evaluator.update_model(statement_model)
        evaluator.run()
    else:
        break




