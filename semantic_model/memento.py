from abc import ABC, abstractmethod
from typing import List
from semantic_model.data import Data
from dsl.evaluator import Evaluator
import inspect



# https://refactoring.guru/design-patterns/memento/python/example



class Originator(ABC):
    """
    This abstract class holds the current state of the
    analysis flow, consisting of one or more Data objects.

    It defines one method for saving the state inside a
    memento, and another method for restoring the state
    from a memento.

    The class is abstract because in order to implement it,
    you need to choose between one of two implementations:
    one for data mementos (saving the state of the data)
    and another for function mementos (saving the functions)

    """

    @abstractmethod
    def set_state(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def restore(self):
        pass

class DataOriginator(Originator):
    """
    This class extends the originator class.
    It implements originator in a way that
    saves the state of the Data object. This approach
    is to be preferred if the size of your data is small.
    """
    def __init__(self, state) -> None:
        self.state = state

    def set_state(self, new_state, func=lambda x: x) -> None:
        self.state = func(new_state)
        self.func = func

    def save(self):
        return ConcreteMemento(self.state, self.func)

    def restore(self, memento):
        self.state = memento.get_data()

class EvaluatorOriginator(Originator):
    """
    TODO: figure out whch originator to use
    This class extends the originator class.
    It implements originator in a way that
    saves the evaluator of the grammar object. This approach
    is to be preferred if you have multiple data objects.
    """
    def __init__(self, state) -> None:
        self.state = state
        self.func=None

    def set_state(self, new_state, func=lambda x: x) -> None:
        self.state = new_state
        self.func = func

    def save(self):
        return ConcreteMemento(self.state, self.func)

    def restore(self, memento):
        self.state = memento.get_data()



# TODO: implement FunctionOriginator - will leave this until later on
class FunctionOriginator(Originator):
    """
    This class extends the originator class. It implements
    originator in a way that saves the function call,
    rather than the state of the data itself. This means
    you don't end up with multiple copies of the data, so
    you can easily rewind.
    """
    def __init__(self, state):
        self.state = state
        self.function = ['init']

    def set_state(self, func):
        self.function += func

    def save(self):
        return ConcreteMemento(self.function)

    def restore(self, memento):
        self.state = memento.get_data()


class Memento(ABC):
    """
    This interface provides a way to access the metadata
    of the memento - i.e. name of the memento, time, place.
     in the order. It also provides methods to get the state.
    """
    _transformations = []
    _id = 0

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_transformations(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

# TODO: add in implementation of the Memento

class ConcreteMemento(Memento):

    def __init__(self, data: Data = None, func=None) -> None:
        self.data = data
        self.func = func
        super()._transformations.append(func) if func is not None else None
        self.transformations = super()._transformations
        self.id = Memento._id
        Memento._id += 1

    def get_name(self) -> str:
        """
        This function is intended to combine the source code of the function that's been
        applied to the state, and returns the new state
        :return:
        """
        return '-'.join([str(self.id), self.func])

    def get_id(self) -> int:
        return self.id

    def get_transformations(self) -> List:
        return self.transformations

    def get_data(self) -> Data:
        return self.data





class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()

        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        for memento in self._mementos:
            print(memento.get_name())

    def load(self, id : str) -> None:
        memento = [memento for memento in self._mementos
                   if memento.get_id() == id][0]
        self._originator.restore(memento)






if __name__ ==  '__main__':
    d = Data('../examples/iris.csv')
    o = DataOriginator(d)
    c = Caretaker(o)
    o.set_state(d.map(d.get_columns()[0], lambda x: x + 1))
    c.backup()
    print(o.state.count())
    o.set_state(o.state.filter(d.get_columns()[0], lambda x: x < 3))
    print(o.state.count())
    c.backup()
    c.show_history()
    c.load(0)
    print(o.state.count())