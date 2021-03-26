from eda import eda_config
import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import plotly.express as px
from matplotlib import pyplot as plt


def plot_score(df,turbine_name=eda_config.TURBINE_NAME, start_time=eda_config.START_TIME, end_time=eda_config.END_TIME, parent_dir = eda_config.PLOT_FOLDER, show_save=eda_config.PLOT_OPTION, colorscale=eda_config.COLORSCALE):
    '''
    Plot anomaly probabilities for one designated turbine and all its tags in a specified time range
    Parameters:
    -----------
    turbine_name: str
        A string indicating turbine name, e.g. '1528-07'
    df: dataframe
        A dataframe storing a set of dataframes as values with keys as turbine names and training_labels column
        (1: anomalous; -1: normal; 0: unknown; unlabeled)
    start_time: str
        The start time of x-axis of the time series plot
    end_time: str
        The end time of x-axis of the time series plot  
    parent_dir: str
        The parent directory that a new folder will be created for storing plots
    show_save: str
        Determine display the plots in the notebook ('show'), or save into a folder ('save')
    Return:
    -------
    '''
    turbine_df = df[(df['turbine_name'] == turbine_name) & (df['ts'] > start_time) & (df['ts'] <= end_time)]
    
    directory = 'anomaly_probs_'+ turbine_name

    path = os.path.join(parent_dir, directory)
    os.makedirs(path,exist_ok=True)
    
    # take the columns from dataframe and put them in a list
    col_list = list(df.columns[:-5])
    for feature_name in col_list:
        file_name = os.path.join(path,feature_name+'.html')
        
        fig = px.scatter(turbine_df, x="ts", y=feature_name, color='score',color_continuous_scale=colorscale,
                 title=turbine_name +': '+ feature_name)

        if show_save == 'show':
            fig.show()
            #return fig
        elif show_save == 'save':
            fig.write_html(file_name)
        else:
            raise ValueError("Only 'show' and 'save' are allowed")
            
def plot_ssdo_predicted_labels(df, turbine_name=eda_config.TURBINE_NAME, start_time=eda_config.START_TIME, end_time=eda_config.END_TIME, parent_dir = eda_config.PLOT_FOLDER, show_save=eda_config.PLOT_OPTION,):
    '''
    Plot cluster based predicted labels for one designated turbine and all its tags in a specified time range
    Parameters:
    -----------
    turbine_name: str
        A string indicating turbine name, e.g. '1528-07'
    df: dataframe
        A dataframe storing a set of dataframes as values with keys as turbine names and training_labels column
        (1: anomalous; -1: normal; 0: unknown; unlabeled)
    start_time: str
        The start time of x-axis of the time series plot
    end_time: str
        The end time of x-axis of the time series plot  
    parent_dir: str
        The parent directory that a new folder will be created for storing plots
    show_save: str
        Determine display the plots in the notebook ('show'), or save into a folder ('save')
    -------
    '''
    turbine_df = df[(df['turbine_name'] == turbine_name) & (df['ts'] > start_time) & (df['ts'] <= end_time)]
    turbine_df['predicted_labels'] = turbine_df['predicted_labels'].astype(str)
    directory = 'ssdo-predLabels_'+ turbine_name
    path = os.path.join(parent_dir, directory)
    os.makedirs(path,exist_ok=True)
    # take the columns from dataframe and put them in a list
    col_list = list(df.columns[:-5])
    for feature_name in col_list:
        file_name = os.path.join(path,feature_name+'.html')
        fig = px.scatter(turbine_df, x="ts", y=feature_name, color='predicted_labels',\
                         color_discrete_map={
                                            "1": "red",
                                            "-1": "blue"})
        fig.update_layout(title= turbine_name +': '+ feature_name)
        if show_save == 'show':
            fig.show()
        elif show_save == 'save':
            fig.write_html(file_name)
        else:
            raise ValueError("Only 'show' and 'save' are allowed")