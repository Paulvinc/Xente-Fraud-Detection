# FRAUD DETECTION 

![DeveloperPrince](https://lhstartupmaqer.com/wp-content/uploads/2020/03/Xente-300x213.png)

This is a machine learning project of being able to predict whether a transaction is a fraud or not.
Take note the Dataset is taken from [zindi](https://zindi.africa/competitions/xente-fraud-detection-challenge) from a closed competition.


##
Requirements:
- pyenv with Python: 3.8.5

### Environment

Same procedure as last time...

Use the requirements file in this repo to create a new environment.

```BASH
make setup 

#or 

pyenv local 3.8.5
python -m venv .venv
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

In order to train the model and store test data in the data folder and the model in models run:

```bash
#activate env
source .venv/bin/activate

python train.py  
```

In order to test that predict works on a test set you created run:

```bash
python predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```

## Limitations

development libraries are part of the production environment, normally these would be separate as the production code should be as slim as possible
