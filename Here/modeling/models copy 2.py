from django.db import models
from here.settings import BASE_DIR

import pandas as pd
import os
import joblib

# Create your models here.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


from sklearn import preprocessing

path = os.path.join(BASE_DIR, 'static/')
train = pd.read_csv(path + 'train_model.csv')
test = pd.read_csv(path + 'test_model.csv')

convert_dict = {'lat': float,
                'long': float
               }
train = train.astype(convert_dict)
test = test.astype(convert_dict)

def encode_features(df_train, df_test):  # label encoding for sklearn algorithms
    features = ["Months", "Sex", "Seasone", "Day", "lat", "long"]
    df_combined = pd.concat([df_train[features], df_test[features]])
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df_combined[feature])
        df_train[feature] = le.transform(df_train[feature])
        df_test[feature] = le.transform(df_test[feature])
    return df_train, df_test


def format_name(df):  # Keeping title
    df['Lname'] = df.Name.apply(lambda x: x.split(' ')[0])
    df['NamePrefix'] = df.Name.apply(lambda x: x.split(' ')[1])
    return df


def drop_features(df):  # Dropping useless features
    return df.drop([ 'Name', 'weather'], axis=1)


def transform_features(df):
    df = format_name(df)
    df = drop_features(df)
    return df


train = transform_features(train)
test = transform_features(test)
train_vis = train.copy(deep=True)  # data for visualization
train, test = encode_features(train, test)
#train.head()

X_all = train.drop(['Survived', 'PassengerId'], axis=1)
y_all = train['Survived']

num_test = 0.20
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=num_test, random_state=23)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV

# Choose the type of classifier.
clf = RandomForestClassifier()

# Choose some parameter combinations to try
parameters = {'n_estimators': [4, 6, 9],
              'max_features': ['log2', 'sqrt','auto'],
              'criterion': ['entropy', 'gini'],
              'max_depth': [2, 3, 5, 10],
              'min_samples_split': [2, 3, 5],
              'min_samples_leaf': [1,5,8]
             }

# Type of scoring used to compare parameter combinations
acc_scorer = make_scorer(accuracy_score)

# Run the grid search
grid_obj = GridSearchCV(clf, parameters, scoring=acc_scorer)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
clf = grid_obj.best_estimator_

# Fit the best algorithm to the data.
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
#print(accuracy_score(y_test, predictions))


joblib.dump(clf, "modeling/logistic_model")
'''
loaded_model = joblib.load('modeling/logistic_model')
#print(loaded_model)
'''
