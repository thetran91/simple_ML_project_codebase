# Step 1  :

## Evironment setup
conda create -p venv python==3.8 -y
conda activate venv/

## setup.py --> create ML applications as a package --> allow other install the projects as packages --> deploy to pypi
search python setup scripts --> for more information

## requirements.txt
#-e . --> automatically trigger setup.py, Search: setup.py and -e. 

## src folder and build the package (turn this application into the package)


# Step 2 :

## src/compopents package
- create __init__.py to call components as a package in or out of the application
- data_ingestion/ data_transformation/ model_trainer

## src/pipeline
- __init__.py to call components as a pipeline
- train_pipeline --> for training process
- predict_pipeline --> for prediction process
- utils.py --> support functions for other files
- logger.py --> log the results --> check logger: python logger.py --> log file will be created in logs folder
Testing:
if __name__ == "__main__":
    logging.info("Logging is started")

- exception.py --> log the exception: Built-in exception/Custom exception
Testing:


# Step 3: Transform from Notebooks to components files
- data_ingestion/ data_transformation/ model_trainer
- Hyperparameter in model_trainer --> hyperparameter other models 
- --> normally we should do hyperparameter in mlops or jupyter notebook to get the best model --> just use the best model in model_trainer.
- Deploy all components --> AWS ec2

# Step 4: Create Prediction Pipeline Using Flask Web APP
- Create application.py using html template files from templates folder
- Using Flask --> Web app 
- python application.py --> run in local host port 5000, localhost:5000/predictdata
