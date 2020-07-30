from utils.function_utils import *
import pandas as pd
from pandas.testing import assert_frame_equal




def test_cartesian_product_single_df():
    df1 = pd.DataFrame([1,1])
    dfs = [df1]
    assert_frame_equal(cartesian_product(dfs), df1)

# def test_cartesian_product_two_df():
#     df1 = pd.DataFrame([[1], [1]], columns=['x'])
#     df2 = pd.DataFrame([[2], [2]], columns=['y'])
#     df3 = pd.DataFrame([[1,2], [1,2], [1,2], [1,2]], columns=['y', 'x'])
#     dfs = [df1, df2]
#     assert_frame_equal(cartesian_product(dfs), df3)
#
# def test_cartesian_product_three_df():
#     df1 = pd.DataFrame([1])
#     df2 = pd.DataFrame([2])
#     df3 = pd.DataFrame([3])
#     df4 = pd.DataFrame([[1,2],[1,3],[2,3]])
#     dfs = [df1, df2, df3]
#     assert_frame_equal(cartesian_product(dfs), df4)






