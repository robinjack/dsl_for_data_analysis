from abc import ABC, abstractmethod


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
    def __init__(self, state):
        self.state=state

    def set_state(self, new_state):
        self.state=new_state

    def save(self):
        return ConcreteMemento(self.state)

    def restore(self, memento):
        self.state = memento.get_data()




class FunctionOriginator(Originator):
    """
    This class extends the originator class. It implements
    originator in a way that saves the function call,
    rather than the state of the data itself. This means
    you don't end up with multiple copies of the data, so
    you can easily rewind.
    """
    def __init__(self):
        pass



class Memento(ABC):
    """
    This interface provides a way to access the metadata
    of the memento - i.e. name of the memento, time, place.
     in the order. It also provides methods to get the state.
    """
    _transformations = []
    _id=0

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
    def __init__(self, data=None, func=None):
        self.data = data
        super()._transformations.append(func) if func is not None else None
        self.id = super()._id
        super()._id+=1
    i




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




