from sklearn.base import BaseEstimator, TransformerMixin
import importlib

# utility function
def check_capping(column, display_head=True, rows=5):
    if display_head:
        return column.value_counts().sort_index().head(rows).rename('count').reset_index()
    else:
        return column.value_counts().sort_index().tail(rows).rename('count').reset_index()


def reset_helper(module):
    importlib.reload(module)


def display_scores(scores):
    print("Scores: ", scores)
    print("Mean: ", scores.mean())
    print("Stadard deviation: ", scores.std())

# custom transformer class
# A custom transformer that only selects
# numerical columns, or categorical columns
class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, type_list=['number']):
        self.type_list = type_list
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return X.select_dtypes(include=self.type_list).to_numpy()

class ColumnDropper(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_drop=[]):
        self.columns_to_drop = columns_to_drop
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return X.drop(columns=self.columns_to_drop)