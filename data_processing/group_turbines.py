import pandas as pd
from data_processing import data_processing_config

def rename_columns(df):
    """
    Rename columns to tag suffix only (removes tag prefix and identifer i.e. (1528-07))
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe with ts and feature columns with prefix and suffix
    Return:
    -------
    pandas.DataFrame
        A new dataframe with updated column names with tag suffix only
    """
    turbine_col = []
    for i in df.columns:
        if i == "ts":
            turbine_col.append("ts")
        else:
            strings = i.split('-')[2:]
            separator = '-'    
            substring = separator.join(strings)
            turbine_col.append(substring)
    df.columns = turbine_col
    
    return df

def sort_columns_alp(df):
    """
    Sort the columns of a dataframe alphabetically
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe with ts and feature columns
    Return:
    -------
    pandas.DataFrame
        A new dataframe with alphabetically ordered column names
    """
    return df.reindex(sorted(df.columns), axis=1)


# sample usage: extract_turbines(dataset, ['1528-07','1528-22','1528-43']) #a dict with 3 dataframes, 1 for each turbine
def extract_turbines(df, turbine_names= data_processing_config.GROUP_TURBINE_NAME_LIST):
    """
    Takes the whole dataset, and creates a dictionary with selected turbines (1 dataframe per turbine)
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe with ts and feature columns
    turbine_names: list of str
        The list of turbine names to extracted
    Return:
    -------
    dict
        A dictionary storing a set of dataframes as values with keys as turbine names
    """
    group_dict = dict()
    for i in turbine_names:
        turbine_cols = [col for col in df.columns if i in col]
        turbine_df = df[turbine_cols]
        ls_ignore = ['BAT01-CE300-XQ20','BAT01-CE300-XQ10','BAT01-CE300-XQ60']
        cols = turbine_df.columns.str.contains('|'.join(ls_ignore))
        turbine_df = turbine_df.loc[:,~cols]
        turbine_df = rename_columns(turbine_df)
        
        turbine_df.insert(loc=0, column='ts', value=df.ts)
        turbine_df['turbine_name'] = i
        df1 = sort_columns_alp(turbine_df)
        group_dict[i] = df1
        print("Turbine " + i + " has been added to the dictionary.")
    return group_dict