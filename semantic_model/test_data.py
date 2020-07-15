from semantic_model.data import *
import pandas as pd
from sklearn.linear_model import LogisticRegression
# setup test dataset

test_data = Data('examples/iris.csv')
df = pd.read_csv('examples/iris.csv')



def test_set_target():
    test_data.set_target('petal_width')
    assert len(test_data.Y_train) == len(test_data.X_train)
    assert len(test_data.Y_test) == len(test_data.X_test)


def test_set_model():
    set_model_test_data = deepcopy(test_data)
    set_model_test_data.set_model(LogisticRegression())
    assert type(set_model_test_data.model)==type(LogisticRegression())

def test_get_data():
    assert str(test_data.data) == str(test_data.get_data())

def test_get_columns():
    assert list(test_data.get_columns()) == ['Unnamed: 0',
                                             'sepal_length', 'sepal_width', 'petal_length',
                                             'petal_width', 'species']


def test_summary():
    assert str(test_data.summary()) == str(test_data.data.sum())


def test_count():
    assert test_data.count().values[0] == len(test_data.data.values)


def test_view():
    assert str(test_data.data.head(5)) ==str(test_data.view())


def test_map():
    vals = [x+1 for x in test_data.data.sepal_length.values]
    mapped_data =  test_data.map('sepal_length', lambda x: x+1)
    assert sum(vals) == sum(mapped_data.data.sepal_length.values)

def test_filter():
    filtered_data = test_data.filter('sepal_length', lambda x: x < 3)
    assert len(filtered_data.data) < len(test_data.data)


def test_train():
    trained_data = test_data.train()
    assert trained_data.trained


def test_test():
    tested_data = deepcopy(test_data)
    tested_data.set_target('petal_width')
    tested_data.train()
    tested_data.test()
    assert 'predict_petal_width' in tested_data.X_test.columns


def test_score():
    tested_data = deepcopy(test_data)
    tested_data.set_target('petal_width')
    tested_data.train()
    tested_data.test()
    print(tested_data.score())


