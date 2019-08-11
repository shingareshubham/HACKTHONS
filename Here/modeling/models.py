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
train = pd.read_csv(path + 'train.csv')
test = pd.read_csv(path + 'test.csv')

'''
def encode_features(df_train, df_test):  # label encoding for sklearn algorithms
    features = ['Fare', 'Cabin', 'Age', 'Sex', 'Lname', 'NamePrefix']
    df_combined = pd.concat([df_train[features], df_test[features]])
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df_combined[feature])
        df_train[feature] = le.transform(df_train[feature])
        df_test[feature] = le.transform(df_test[feature])
    return df_train, df_test


def simplify_ages(df):  # Binning ages
    df.Age = df.Age.fillna(-0.5)
    bins = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
    group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
    categories = pd.cut(df.Age, bins, labels=group_names)
    df.Age = categories
    return df


def simplify_cabins(df):  # Storing first letter of cabins
    df.Cabin = df.Cabin.fillna('N')
    df.Cabin = df.Cabin.apply(lambda x: x[0])
    return df


def simplify_fares(df):  # Binning fares
    df.Fare = df.Fare.fillna(-0.5)
    bins = (-1, 0, 8, 15, 31, 1000)
    group_names = ['Unknown', '1_quartile', '2_quartile', '3_quartile', '4_quartile']
    categories = pd.cut(df.Fare, bins, labels=group_names)
    df.Fare = categories
    return df


def format_name(df):  # Keeping title
    df['Lname'] = df.Name.apply(lambda x: x.split(' ')[0])
    df['NamePrefix'] = df.Name.apply(lambda x: x.split(' ')[1])
    return df


def drop_features(df):  # Dropping useless features
    return df.drop(['Ticket', 'Name', 'Embarked'], axis=1)


def transform_features(df):
    df = simplify_ages(df)
    df = simplify_cabins(df)
    df = simplify_fares(df)
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
raw_data = {'Pclass': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'Sex': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'Age': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'SibSp': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'Parch': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'Fare': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'Cabin': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'Lname': [1, 0, 3, 0, 0, 3, 1, 767, 20],
            'NamePrefix': [1, 0, 3, 0, 0, 3, 1, 767, 20]}

df = pd.DataFrame(raw_data, columns=["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Cabin", "Lname", "NamePrefix"])


loaded_model = joblib.load('modeling/logistic_model')

#result = loaded_model(df)
#print(loaded_model)


class titanic(models.Model):
    Pclass = models.IntegerField()
    Sex = models.IntegerField()
    Age = models.IntegerField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare = models.IntegerField()
    Cabin = models.IntegerField()
    Lname = models.IntegerField()
    NamePrefix = models.IntegerField()

class predictive(models.Model):
    Pclass = models.IntegerField()
    Sex = models.IntegerField()
    Age = models.IntegerField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare = models.IntegerField()
    Cabin = models.IntegerField()
    Lname = models.IntegerField()
    NamePrefix = models.IntegerField()

from django.db import models
import pandas as pd
from modeling.models import titanic

# Create your models here.
from django_pandas.io import read_frame
qs = titanic.objects.all()
df = read_frame(qs)
print(df)