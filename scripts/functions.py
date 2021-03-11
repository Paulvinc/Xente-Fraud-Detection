#please copy paste your functions here, don't forget to import the necessary libraries that are required when running your functions


import pandas as pd


"""def changedate(df, datetime_lst):
    for i in datetime_lst:
        df[i]=pd.to_datetime(df[i])
    return df"""
    

def remove_columns(df, drop_lst): #name dataframe, list of columns
    remaining_features = [x for x in df.columns if x not in drop_lst]
    df = df[remaining_features]
    return df


def make_categories(df, cat_lst): #dataframe, list of columns we want to change
    for i in cat_lst:
        df[i]=df[i].astype('category')
    return df


def make_dummies(df, dummy_lst): 
    for i in dummy_lst:
        if str(df[i][1]).isnumeric():
            dummies = pd.get_dummies(df[i], prefix=str(i), drop_first=True) 
        else:
            dummies = pd.get_dummies(df[i], drop_first=True) #if the values in original column contains name, don't need prefix
        df = df.drop([i], axis=1)
        df = pd.concat([df, dummies], axis=1)
    return df


from imblearn.over_sampling import SMOTE #require the instalation imblearn library, available in requirement.txt
from imblearn import under_sampling, over_sampling

def balance_traindata(X_train, y_train):
    '''
    requires 2 parameters: X_train, y_train
    returns: X_train, y_train (with balanced y_train values)
    '''
    # Oversample data
    smote_algo = SMOTE(random_state=0)
    smote_data_X, smote_data_Y = smote_algo.fit_resample(X_train, y_train)
    smote_data_X = pd.DataFrame(data=smote_data_X, columns=X_train.columns)
    smote_data_Y = pd.DataFrame(data=smote_data_Y)
    # Join X and Y smote data into one
    smote_data = smote_data_X
    return smote_data, smote_data_Y[y_test.name]

