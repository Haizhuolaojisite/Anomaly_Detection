import copy
from data_processing import data_processing_config
import pandas as pd

#data_processing
def add_model_columns(df, modelname=data_processing_config.MODEL_NAME):
    """
    Takes a dataframe, and adds three columns with dummy values;
    training_labels: labels to be entered manually, 
    score: calculated score/probablity from model will be stored here,
    predicted_labels: predictions will be stored here for anomatools.
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe
    modelname: str
        A string with the name of the model being used
    Return:
    -------
    pandas.DataFrame
        A new dataframe with 3 additional columns with dummy values.
    """
    #assigning them the proper type dummy values
    if modelname == "ssdo":
        col_val_dict = {
            "training_labels": -2,
            "score": -2.0,
            "predicted_labels": -2
        }
        
    else:
        col_val_dict = {
            "training_labels": 0,
            "score": -2.0,
            "predicted_labels": -2
        }

    tempdf = df.copy()
    for key, value in col_val_dict.items():
        tempdf[key] = value
    return tempdf

def update_training_labels(df, label_list= data_processing_config.LABEL_LIST, modelname= data_processing_config.MODEL_NAME):
    """
    Updates the "training_labels" column values with provided labels.
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe
    label_list: list
        A list that specifies turbine names, date range and labels
    Return:
    -------
    pandas.DataFrame
        A new dataframe with updated labels.
    """
    df = add_model_columns(df, modelname)
    tempdf = df.copy()
    turbine_name = ""
    for each in label_list:
        turbine_name = each[0]
        for i in each:
            if type(i) == list:
                tempdf['training_labels'][(tempdf['turbine_name'] == turbine_name) & (tempdf['ts'] > i[0]) & (tempdf['ts'] <= i[1])] = i[2]
    return tempdf