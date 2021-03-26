"""
Any config specific to model training step goes here.
"""

# path of the source code for PBAD package. It's assumed that this is already installed
# check the readme file for installation steps
PBAD_SC_PATH = "/home/azureuser/cloudfiles/code/Users/kaan.eroglu/pbad/src"

#PBAD: list of columns to be excluded from the model fit.
#this list has to include at least these 5 values: 'ts', 'turbine_name', 'training_labels', 'score', 'predicted_labels'
#if you want to exclude some features from your model fit, add those in this list.
EXCLUDE_COLUMNS = ['ts', 'turbine_name', 'training_labels', 'score', 'predicted_labels']

#SSDO paramaters
#The number of base estimators in the IsolationForest, 150 is tuned values
ESTIMATORS=150

