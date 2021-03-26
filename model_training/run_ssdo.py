from model_training import model_training_config
import pandas as pd

from anomatools.models import SSkNNO, SSDO
from sklearn.ensemble import IsolationForest
from collections import Counter
from sklearn.preprocessing import StandardScaler

def ssdo_build_trainset(group_df):
    '''
    Build the training set for ssdo model
    Parameters:
    -----------
    group_df: dataframe
        A dataframe storing a set of dataframes as values with keys as turbine names and training_labels column
        (1: anomalous; -1: normal; 0: unknown; unlabeled)
    Return:
    -------
    train: dataframe
        A new training dataframe storing a set of labelled dataframes as values with keys as turbine names 
        and training labels (1: anomalous; -1: normal; 0: unknown)
    '''
    # Anomalous dataset
    ano_df = group_df[group_df['training_labels'] == 1]
    # Normal dataset
    nor_df = group_df[group_df['training_labels'] == -1]
    # Unknown dataset
    unknown_df = group_df[group_df['training_labels'] == 0]
    
    # Labelled Dataset
    train = pd.concat([ano_df, nor_df,unknown_df], ignore_index=True)
    
    return train


def run_ssdo(group_df, exclude_columns = model_training_config.EXCLUDE_COLUMNS,estimators=model_training_config.ESTIMATORS):  
    '''
    Train ssdo detector and perform cluser based anomaly detection
    Parameters:
    -----------
    group_df: dataframe
        A labelled dataframe storing a set of dataframes as values with keys as turbine names and training_labels column
    estimator: integer; default=150
        The number of base estimators in the ensemble
    Return:
    -------
    group_df: dataframe
        A new dataframe storing a set of turbine dataframes and anomaly detection results:
        predicted_labels: 1: anomalous; -1: normal
        score: anomaly probability, [0,1]   
    '''
    # Trainset:
    trainset = ssdo_build_trainset(group_df)
    # Train
    # exclude columns you don't want
    X_train = trainset[trainset.columns[~trainset.columns.isin(exclude_columns)]].to_numpy()
    # X_train = trainset[trainset.columns[:-5]].to_numpy()
    Y_train = trainset["training_labels"].values
    # All dataset
    X_all = group_df[group_df.columns[~group_df.columns.isin(exclude_columns)]].to_numpy()
    # X_all = group_df[group_df.columns[:-5]].to_numpy()
    
    # Standardization
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_all = scaler.transform(X_all)
    
    # Contanmination rate:
    counter = Counter(Y_train)
    c = counter[1]/len(Y_train)
    print('comtanination rate = ',c)
    
    # Priors of Isolation Forest
    prior_detector = IsolationForest(n_estimators=estimators, contamination=c)
    prior_detector.fit(X_train)

    tr_prior = prior_detector.decision_function(X_train) * -1
    all_prior = prior_detector.decision_function(X_all) * -1

    tr_prior = tr_prior + abs(min(tr_prior))
    all_prior = all_prior + abs(min(all_prior))
    
    # SSDO
    detector = SSDO(k=30, alpha=2.5, unsupervised_prior='other',contamination=c)

    tr_pred = detector.fit_predict(X_train,Y_train,prior=tr_prior)
    tr_prob = detector.predict_proba(X_train, prior=tr_prior, method='linear')[:, 1]

    all_pred = detector.predict(X_all, prior=all_prior)
    all_prob = detector.predict_proba(X_all, prior=all_prior, method='linear')[:, 1]

    # Model Evaluation:
    print('TRAIN set anomalies:', Counter(tr_pred), '; expected =', int(c * len(X_train)))
    print('All dataset anomalies:', Counter(all_pred), '; expected =', int(c * len(all_pred)))
    print('detector threshold: ',detector.threshold_)
    

    # Add prediction results as 'preds' column in output_df dataset
    group_df['predicted_labels'] = all_pred
    # Add probabilities results as 'probs' column in output_df dataset
    group_df['score'] = all_prob
    
    return group_df