# FRAUD DETECTION 

![DeveloperPrince](https://lhstartupmaqer.com/wp-content/uploads/2020/03/Xente-300x213.png)

This is a machine learning project of being able to predict whether a transaction is a fraud or not.
The Dataset is taken from a closed [Zindi](https://zindi.africa/competitions/xente-fraud-detection-challenge) competition.

Fraud detection is an important application of machine learning in the financial services sector. This solution will help Xente provide improved and safer service to its customers.

This competition is sponsored by Xente, Innovation Village, and insight2impact.

#### **About Xente**

Xente is an e-payments, e-commerce, and financial services company in Uganda offering various products and services that can be paid for using Mobile Money (Airtel Money, MTN Mobile Money), Bank Card (Visa Card, Master Card), Xente wallet and on credit (Pay Later). Some of the products consumers can buy include airtime, data bundles, pay water and electricity bills, TV subscription services, buy event tickets, movie tickets, bus tickets, and more.


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
