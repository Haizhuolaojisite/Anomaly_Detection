import copy
from data_processing import data_processing_config

#impute_feature(turbine_group, "1528-22", "MDY01-CT009-XQ50", mean_for_temp_main)
def impute_feature(turbine_group, new_values, turbine_name=data_processing_config.TURBINE_NAME, feature_id=data_processing_config.FEATURE_ID):
    """
    Impute the values of a turbine's feature
    Parameters:
    -----------
    turbine_group: dict
        A dictionary storing a set of dataframes as values with keys as turbine names 
    turbine_name: str
        A string with the name of the turbine (i.e. "1528-22")
    feature_id: str
        A string with the suffix of the feature to be used for calculation. i.e. "MDY01-CT009-XQ50"
    new_values: pandas.Series
        A pandas series with the values to be used to impute
    Return:
    -------
    dict
        A new dictionary storing a set of dataframes as values with keys as turbine names
    """
    imputed_turbine_group = copy.deepcopy(turbine_group)

    for key, value in imputed_turbine_group.items():
        if key == turbine_name:
            value[feature_id] = new_values.values

    return imputed_turbine_group
    