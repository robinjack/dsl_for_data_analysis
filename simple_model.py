from textx import metamodel_from_file

simple_meta = metamodel_from_file('simple_model.tx')
from semantic_model.data import Data


example_simple_model = simple_meta.model_from_file('simple_model.analysis')

print(example_simple_model)


d = Data(example_simple_model.data.fp)

for c in example_simple_model.command:
    print(c.data)


print(d)