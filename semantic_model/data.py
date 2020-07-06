import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
from ..utils.const import NUMERIC_DATATYPES
from .memento import DataOriginator, FunctionOriginator, ConcreteMemento, AnalysisFlow


"""
The data class exposes an array of methods that 
allows an analyst to perform an analysis.
"""



class Data() :
    # Initialisation + ingestion functions
    def __init__(self, data, model=LinearRegression,
                 test_size=0.33, random_state=42):
        if type(data)==str:
            self.data = pd.read_csv(data)
        else:
            self.data = data

        self.set_model(model)
        self.test_size=test_size
        self.random_state=random_state



    # Configuration for testing
    def set_target(self, y):
        dtypes = self.data.dtypes
        X = self.data[[col for col,dtype in dtypes if col != y and dtype in NUMERIC_DATATYPES ]]
        Y = self.data[[y]]
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
        X, Y, test_size=self.test_size, random_state=self.random_state)

    def set_model(self, model=LinearRegression()):
        self.model = model
        return self

    def get_data(self):
        return self.data

    def get_columns(self):
        return self.data.columns

    def __str__(self):
        return str(self.data.head())

    # Analysis functions


    def summary(self):
        return self.data.sum()

    def count(self):
        return self.data.count()

    def view(self, start_index=0, end_index=5):
        return self.data[start_index:end_index]


    def plot(self):
        return

    # Manipulation functions
    def map(self, col, func):
        self.data[col] = [func(val) for val in self.data[col].values]
        return self

    def filter(self, col, cond):
        self.data = self.data[cond(self.data[col])]
        return self

    # Training functions

    def train(self):
        self.model.fit(self.X_train, self.Y_train)
        return self

    # Testing functions

    def test(self):
        self.data['predict_y'] = self.model.predict(self.X_test, self.Y_test)







