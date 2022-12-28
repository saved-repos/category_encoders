"""
Base IO code for datasets
"""

import pkg_resources
import pandas as pd

def load_compass():
    """Return a dataframe for target encoding with 16 rows of compass directions.

    Contains the following fields:
        index                16 non-null int64
        compass              16 non-null object
        HIER_compass_1       16 non-null object
        target               16 non-null int64

    Returns
    -------
    X: A pandas data frame containing features
    y: A pandas series containing the target variable

    """
    data_filename = "data/compass.csv"
    stream = pkg_resources.resource_filename(__name__, data_filename)

    with open(stream) as f:
        df = pd.read_csv(f, encoding='latin-1')
    X = df[['index', 'compass', 'HIER_compass_1']]
    y = df['target']
    return X, y


def load_postcodes(target_type='binary'):
    """Return a dataframe for target encoding with 100 UK postcodes and hierarchy.

    Contains the following fields:
        index                100 non-null int64
        postcode             100 non-null object
        HIER_postcode1       100 non-null object
        HIER_postcode2       100 non-null object
        HIER_postcode3       100 non-null object
        HIER_postcode4       100 non-null object
        target_binary        100 non-null int64
        target_non_binary    100 non-null int64
        target_categorical   100 non-null object

    Parameters
    ----------
    target_type : str, default='binary'
        Options are 'binary', 'non_binary', 'categorical'

    Returns
    -------
    X: A pandas data frame containing features
    y: A pandas series containing the target variable

    """
    data_filename = "data/postcode_dataset_100.csv"
    stream = pkg_resources.resource_filename(__name__, data_filename)

    with open(stream) as f:
        df = pd.read_csv(f, encoding='latin-1')
    X = df[df.columns[~df.columns.str.startswith('target')]]
    y = df[f'target_{target_type}']
    return X, y