# #### Import Libraries
import sys
from pathlib import Path
from azureml.core import Workspace, Dataset
import warnings
warnings.filterwarnings("ignore")
from data_acquisition import data_acquisition_config


# **NOTE FOR USERS:**    
# It is assumed that all .csv files are imported to the Azure Blob Storage and being read from the Azure workspace. 
# To read a .csv  file directly, pandas **pd.read_csv(file_path)** has to be used instead  

def data_acquisition(subscription_id=data_acquisition_config.SUBSCRIPTION_ID, resource_group=data_acquisition_config.RESOURCE_GROUP, workspace_name=data_acquisition_config.WORKSPACE_NAME, dataset_name=data_acquisition_config.DATASET_NAME):
    '''
    Perform Data Acquisition of wind turbine dataset in Azure Dataset
    Parameters:
    -----------
    subscription_id: str
        The subscription ID of Azure workspacke, e.g. 'f17fb002-6ef1-424c-b174-afccfd751092'
    resource_group: str
        The name of Azure resource group, e.g. 'TransaltaAAILabs'
    workspace_name: str
        The name of Azure workspace_name, e.g. 'Transalta-AAILabs'
    Return:
    -------
    dataset: Dataframe
    '''
    subscription_id = subscription_id
    resource_group = resource_group
    workspace_name = workspace_name

    workspace = Workspace(subscription_id, resource_group, workspace_name)

    dataset = Dataset.get_by_name(workspace, name=dataset_name)
    # Load melancthon data in the notebook and assign the 'dataset'.
    dataset = dataset.to_pandas_dataframe() #.set_index('ts')
    
    return dataset
