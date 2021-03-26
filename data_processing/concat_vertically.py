import pandas as pd

def concat_vertically(turbine_group):
    """
    Concatanate multiple dataframes vertically. Assumes the order of columns names are the same for all dataframes.
    Parameters:
    -----------
    turbine_group: dict
        A dictionary storing a set of dataframes as values with keys as turbine names 
    
    Return:
    -------
    pandas.DataFrame
        A dataframe with vertically concataned dataframes
    """
    df = pd.concat([df for df in turbine_group.values()], ignore_index=True, axis=0)
    return df