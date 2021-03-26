"""
Run pipeline by calling this file with "python run_pipeline.py pbad"
TO run with imputation "python run_pipeline.py pbad impute"
"""

import os
import sys
import pandas as pd
import argparse
from pathlib import Path
from data_acquisition.data_acquisition import data_acquisition
from data_processing.group_turbines import extract_turbines
from data_processing.calculate_mean import calculate_mean
from data_processing.impute_feature import impute_feature
from data_processing.concat_vertically import concat_vertically
from data_processing.populate_labels import update_training_labels
from model_training.run_pbad import run_pbad
from model_training.run_ssdo import run_ssdo
from eda.plot_model_results import plot_score
from eda.plot_model_results import plot_ssdo_predicted_labels

#assign model name to the first argument from command line
model_name = sys.argv[1]

#if there is a second argument from command line, check if it is equal to "impute"
if len(sys.argv)>2:
    if sys.argv[2] == "impute":
        isImpute = True
    else:
        isImpute = False
else:
    isImpute = False

def run_pipeline():
    print(">>> Starting the pipeline!")
    dataset = data_acquisition()
    print(">>> Extracting selected turbines...")
    turbine_group = extract_turbines(dataset)
    
    if isImpute:
        print(">> Imputation is enabled.")
        print(">>> Calculating mean and imputing the requested feature...")
        mean_for_temp_main = calculate_mean(turbine_group)
        turbine_group= impute_feature(turbine_group, mean_for_temp_main)
    else:
        print("Imputation is disabled")

    print(">>> Concatenating selected turbines vertically...")
    
    concat_turbine_group = concat_vertically(turbine_group)
    print(">>> Updating training labels...")
    df2model = update_training_labels(concat_turbine_group)
    print(">>> Running the model... This might take a while...")
    if model_name == "pbad":
        print("PBAD")
        df2plot = run_pbad(df2model)
    elif model_name == "ssdo":
        print("SSDO")
        df2plot = run_ssdo(df2model)
    print(">>> Exporting the plots...")
    plot_score(df2plot)
    
if __name__ == "__main__":
    run_pipeline()