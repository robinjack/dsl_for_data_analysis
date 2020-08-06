import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix



"""In this file, we have:
1. Functions associated with plotting
2. plot_dict mapping 


TODO: add in further plotting kinds. For example, histograms,
scatter plots, box plots, bar charts - and so forth.

"""



def pairs_plot(data=None):
    return scatter_matrix(data.data,
                          # c=data.Y_train,
                          figsize=(15, 15), marker='o',
                      hist_kwds={'bins': 20}, s=60, alpha=.8)



KIND_TO_PLOT_FUNC_DICT = {
    'pairs' : pairs_plot
}