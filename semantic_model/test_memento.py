from semantic_model.memento import *
import pandas as pd


test_data = Data('examples/iris.csv')


"""
This file tests the originator class.

  

"""

##########################################
# Originator unit tests
##########################################


def test_init_originator():
    o = DataOriginator(test_data)
    assert o


def test_data_originator():
    o = DataOriginator(test_data)
    assert o.state == test_data

def test_evaluator_originator():
    o = EvaluatorOriginator(test_data)
    assert o.state == test_data

def test_function_originator():
    o = FunctionOriginator(test_data)
    assert o.state == test_data

# Test the functions of the evaluator originatr
def test_set_state():
    o = EvaluatorOriginator(test_data)
    o.set_state(1)
    assert o.state == 1

def test_save():
    o = EvaluatorOriginator(test_data)
    o.set_state(1)
    firstMemento = o.save()
    secondMemento = o.save()
    assert type(firstMemento) == ConcreteMemento
    assert firstMemento.get_id() == 0
    assert secondMemento.get_id() == 1
    assert firstMemento.get_data() == secondMemento.get_data()


def test_restore():
    o = DataOriginator(test_data)
    firstMemento = o.save()
    o.set_state(1)
    o.restore(firstMemento)
    assert o.state == test_data

# test the functions of the ConcreteMemento


def test_init_concreteMemento():

    fourthMemento = ConcreteMemento()
    fifthMemento = ConcreteMemento()
    sixthMemento = ConcreteMemento()
    seventhMemento = ConcreteMemento()

    assert fourthMemento.get_id() == 3
    assert seventhMemento.get_id() == 6


def test_get_data_concreteMemento():
    a = ConcreteMemento()
    assert a.get_data() is None
    b = ConcreteMemento(test_data)
    assert b.get_data() == test_data



# Assess the workings of the caretaker

def test_init_caretaker():
    o = DataOriginator(test_data)
    c = Caretaker(o)

    assert c._mementos == []
    assert c._originator == o

def test_backup():
    o = DataOriginator(test_data)
    c = Caretaker(o)

    c.backup()
    o.set_state(test_data.summary())
    c.backup()
    assert len(c._mementos) == 2
    assert type(c._mementos[0]) == ConcreteMemento


def test_undo():
    o = DataOriginator(test_data)
    c = Caretaker(o)

    c.backup()
    o.set_state(test_data.summary())
    c.undo()
    assert o.state == test_data


