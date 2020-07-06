from semantic_model.data import *
import pandas as pd
from sklearn.linear_model import LogisticRegression
# setup test dataset

test_data = Data('iris.csv')
df = pd.read_csv('iris.csv')



def test_set_target():
    test_data.set_target('petal_width')
    assert len(test_data.Y_train) == len(test_data.X_train)
    assert len(test_data.Y_test) == len(test_data.X_test)


def test_set_model():
    assert test_data.model == LinearRegression()
    test_data.set_model(LogisticRegression())
    assert test_data.model == LogisticRegression()

def test_get_data():
    assert test_data.data == test_data.get_data()

def test_get_columns():
    assert list(test_data.get_columns()) == ['Unnamed: 0', 'sepal_length', 'sepal_width', 'petal_length',
       'petal_width', 'species']

def test_summary():
    assert False

def test_count():
    assert False

def test_view():
    assert False

def test_plot():
    assert False

def test_map():
    assert False

def test_filter():
    assert False

def test_train():
    assert False

def test_test():
    assert False

