from .memento import *
from .data import *
from ..utils.const import ORIGINATOR_TYPES


"""
The Data class exposes an API for us to perform analysis.
The Memento class exposes a way for us to record the 
actions that have happened
The analysis flow exposes a way for us to connect the two.
"""


# TODO: we may not actually need an analysis flow type, figure out if this is true


class AnalysisFlow(Data):
    def __init__(self, data, originator_type='data'):
        super().__init__(data)
        self.originator=eval(ORIGINATOR_TYPES[originator_type])()
        self.caretaker = Caretaker(self.originator)


    def AnalysisFlowDecorator(func):
        def wrapper(x):

            func(x)