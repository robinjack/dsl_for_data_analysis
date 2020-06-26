import pandas as pd
from sklearn import datasets
import seaborn as sns
from sklearn.model_selection import train_test_split






class Data():
    def __init__(self, data):
        if type(data)=='str':
            self.data = pd.read_csv(data)
        else:
            self.data = data

    def get_data(self):
        return self.data

    def set_target_col(self, y):
        X = self.data[[x for x in self.data.columns if x != y]]
        Y = self.data[[y]]
        self.X_train, self.X_test, self.Y_train, self.T_test = train_test_split(
        X, Y, test_size = 0.33, random_state = 42)


iris = sns.load_dataset('iris')

d = Data(iris)


print(d.get_data().head())




