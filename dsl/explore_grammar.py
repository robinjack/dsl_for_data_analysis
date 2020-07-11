from textx import metamodel_from_file
from semantic_model.data import Data
# from dsl.expression_parser.expression import ast


meta = metamodel_from_file('analysis_flow.tx')
test_model = meta.model_from_file('../examples/test_ae2.analysis')

print(1)


