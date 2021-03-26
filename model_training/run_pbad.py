# try loading the relevant methods
from model_training import model_training_config
import sys, os, time
import pandas as pd
try:
    sys.path.insert(0, model_training_config.PBAD_SC_PATH)
except:
    print('Failed to add path')
    pass

from sklearn.metrics import roc_auc_score
from sklearn.ensemble import IsolationForest

from methods.PreProcessor import PreProcessor
from methods.PBAD import PBAD
from baselines.PAV import PAV
from baselines.FPOF import FPOF
from baselines.MPAD import MPAD

#ts, labels = pbad_data_prep(df2model)
def pbad_data_prep(df, exclude_columns = model_training_config.EXCLUDE_COLUMNS):
    """
    Extracts values from each feature and puts them in the right format for PBAD
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe
    exclude_columns: list
        A list that specifies columns to be excluded. If some of the features need to be excluded, it should be provided here along with the default ones.
    Return:
    -------
    dict, numpy.ndarray
        A new dictionary with values of features for the whole time series (values are np arrays)
        A numpy array with labels for the whole time series
    """
    # create a list of np array with values from each feature
    emptylist = []
    for column in df:
        if column not in exclude_columns:
            emptylist.append(df[column].values)
    #create a list of ints goes from 0 to number of features
    a = list(range(0, len(emptylist)))
    #create a dicrionary with numpy arrays (1 key/pair values for each turbine)
    ts = {e: emptylist[i] for i, e in enumerate(a)}
    #extract labels
    labels = df["training_labels"].values
    return ts, labels

#ts_windows_discretized, ts_windows = pbad_preprocess_data(ts, labels, window_size_incr)
def pbad_preprocess_data(ts, labels, window_size_incr, alphabet_size=30):
    """
    Runs the preprocessor for PBAD.
    Parameters:
    -----------
    df: pandas.DataFrame
        A dataframe
    exclude_columns: list
        A list that specifies columns to be excluded. If some of the features need to be excluded, it should be provided here along with the default ones.
    Return:
    -------
    dict, dict
        Two dictionaries of numpy arrays for discretized windows and windows
    """
    preprocesser = PreProcessor(window_size=window_size_incr, window_incr=window_size_incr, alphabet_size=30)
    ts_windows_discretized, ts_windows, _, window_labels = preprocesser.preprocess(continuous_series=ts, labels=labels,return_undiscretized=True)
    return ts_windows_discretized, ts_windows

#scores = run_pbad(ts_windows_discretized, ts_windows)
def run_pbad_fit(ts_windows_discretized, ts_windows, relative_minsup=0.01, jaccard_threshold=0.9, pattern_type='all', pattern_pruning='maximal'):
    """
        Runs the PBAD model.
        Parameters:
        -----------
        ts_windows_discretized: dict
            A dictionary of numpy arrays for discretized windows
        ts_windows: dict
            A dictionary of numpy arrays for windows 
        Return:
        -------
        numpy.ndarray
            A numpy array of calculated anomaly scores
    """
    pbad = PBAD(relative_minsup=relative_minsup, jaccard_threshold=jaccard_threshold, pattern_type=pattern_type, pattern_pruning=pattern_pruning, verbose=False)
    scores = pbad.fit_predict(ts_windows, ts_windows_discretized)
    return scores

#df2plot = pbad_post_process_data(df2model, scores, window_size_incr)
def pbad_post_process_data(df2model, scores, window_size_incr):
    """
        Processes results back into a dataframe.
        Parameters:
        -----------
        df: pandas.DataFrame
            A dataframe
        scores: numpy.ndarray
            A numpy array of calculated anomaly scores 
        window_size_incr:
            An integer defining the windows size and window increment. Should match the number used in the model
        Return:
        -------
        pandas.DataFrame
            A dataframe with all feature values and anomaly scores
    """
    #copy scores into a dataframe
    dfscores = pd.DataFrame(data=scores)
    #unpack scores into a list - 1 score per row
    scorelist = []
    for i, j in dfscores.iterrows(): 
        for each in list(range(0, window_size_incr)):
            scorelist.append(j.values[0])
    #create a copy of the dataframe, and overwrite scores into score column
    df2plot = df2model.copy()
    df2plot["score"] = scorelist
    return df2plot

def run_pbad(df, exclude_columns = ['ts', 'turbine_name', 'training_labels', 'score', 'predicted_labels'], window_size_incr=12, alphabet_size=30, relative_minsup=0.01, jaccard_threshold=0.9, pattern_type='all', pattern_pruning='maximal'):
    """
        Runs the PBAD pipeline.
        Parameters:
        -----------

        Return:
        -------
 
    """
    print("--> Running the data preperation step. This extracts values from each feature and puts them in the right format for PBAD.")
    ts, labels = pbad_data_prep(df, exclude_columns=exclude_columns)
    print("-->Running the preprocessor for PBAD.")
    ts_windows_discretized, ts_windows = pbad_preprocess_data(ts, labels, window_size_incr=window_size_incr)
    print("This might take up to 12 minutes")
    print("--> Fitting the PBAD model.")
    scores = run_pbad_fit(ts_windows_discretized, ts_windows, relative_minsup=relative_minsup, jaccard_threshold=jaccard_threshold, pattern_type=pattern_type, pattern_pruning=pattern_pruning)
    print("--> Running the post-processing step to put everything back into a dataframe")
    df2plot = pbad_post_process_data(df, scores, window_size_incr)
    return df2plot
    