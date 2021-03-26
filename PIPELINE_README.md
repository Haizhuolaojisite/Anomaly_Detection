# How to Use the Template

The `train_pipeline.py` runs Data Acquisition, Data Processing, Data Validation, Model Training and Model Validation
Components and saves the trained model artifact in output directory.

The Train Pipeline can be run on Azure or locally, as specified in `config.py`. All global configurations such as model
name and path to the output directory go into this file. When running on Azure, the experiment and model artifact are
also logged in Azure workspace.

All of the following folders contain a config file that should be used for specific configuration of that folder.
They also contain a `main.py` file that should be used to perform the tasks specific to that folder:
- data_acquisition
  * Data acquisition should be done in `get_data()` function of `data_acquisition/main.py`.
  Moreover, `get_hold_out_data()` should be used to provide a hold out test set.

    **Note:** `data` folder that contains all the raw data files exist on this folder and **not** the root directory.
- data_processing
  * Given raw data in any format, data processing should be done in `process_data()` function of
  `data_processing/main.py`.
- data_validation
  * Data validation checks should be performed in `validate_data()` function of `data_validation/main.py`
- model_training
  * Model creation should be done in `train_model()` function of `model_training/main.py`. Model selection,
  hyper parameter selection and metric logging should all be handled in this file.
- model_validation
  * To check if the model is ready for registration, use `validate_model()` function of `model_validation/main.py`.

If you want to run the pipeline on Azure, add experiment name (`EXPERIMENT_NAME`) and model name (`MODEL_NAME`) to
`azure/azure_config.py`. Azure compute cluster information can stay the same or be modified according to your needs.

### Example
If you wanna see an example, `examples/generate_sample_data.py` file generates an input and hold out dataset which can
be used to train a model. Run `python3 examples/generate_sample_data.py` to create these files.


First, you need to place the generated files in `data_acquisition/data` folder and provide the file names in
`data_acquisition/data_acquisition_config.py`.
```python
INPUT_DATA_NAME = 'breast_cancer_data.csv'
HOLD_OUT_DATA_NAME = 'breast_cancer_data_holdout.csv'
```

 You also need to provide appropriate names in `azure/azure_config.py` (if you want to run it on azure):
```python
EXPERIMENT_NAME = 'Demo_breast_cancer_data'
MODEL_NAME = 'model_breast_cancer'
```
or `config.py` (if you want to run it locally):
```python
MODEL_NAME = 'breast_cancer_model'
```

# How to Run The Pipeline

1. Specify `COMPUTE` type (`azure` or `local`) in config file. When running on azure, you need to download and save the
Azure workspace configuration and save it in `.azureml`, or in a parent directory.

2. To run the pipeline without docker environment, install required Python packages in `requirements.txt` and start the
pipeline with `python3 train_pipeline.py` command

- **Note:** If you want to run the pipeline locally, you can remove Azure dependencies from `requirements.txt`.

3. To run the pipeline using docker environment, start the pipeline using
`sudo bash docker/run_docker_train_pipeline.sh` command.

Notes:
 - When running on Azure, the CLI will prompt for authentication first time it is run.
 - The Trained model artifact will be in `OUTPUT_DIR`.
 - Once pipeline is run to train the model, the following files will be saved in `OUTPUT_DIR` directory:
   1. `model_name.pkl`: Trained model file.
   2. `requirements.txt` The required packages to use the trained model.
   3. `input-config.yaml`. This file contains information about features used to train the model
 - When running on Azure Pipeline, the above files will be uploaded to the pipeline run outputs directory too.
