import copy

import pandas as pd
from data_processing import data_processing_config

def calculate_mean(turbine_group, exclude_from_mean_list = data_processing_config.EXCLUDE_FROM_MEAN_LIST, feature_id = data_processing_config.FEATURE_ID):
    """
    Calculate the mean values of a feature from a set of turbines
    Parameters:
    -----------
    turbine_group: dict
        A dictionary storing a set of dataframes as values with keys as turbine names 
    exclude_from_mean_list: list of str
        The list of turbine names to be excluded from calculation. If it is empty, all turbines in turbine_group will be used
    feature_id: str
        A string with the suffix of the feature to be used for calculation. i.e. "MDY01-CT009-XQ50"
    Return:
    -------
    pandas.Series
        Mean values calculated from a set of turbines
    """
    meandf = next(iter(turbine_group.values())) #gets the first value(df) in a dict
    meandf = meandf[['ts']].copy() #get rid of all other cols, except ts

    for key, value in turbine_group.items():
        if key in exclude_from_mean_list:
            print("Turbine " + key + " is excluded. the value is not used.")
        else:
            meandf[key] = value[feature_id].values
            print("The value of feature " + feature_id + " on Turbine " + value["turbine_name"][0] + " was extracted for mean calculation." )
    
    tempmean = meandf.loc[:, meandf.columns != 'ts']
    tempmean['mean'] = tempmean.mean(axis=1)
    meandf['mean'] = tempmean['mean']
    return(meandf['mean']) #return mean values only -as panda dataseries
    #return(meandf) #return the df with ts,  all values and mean