import os
import pandas as pd
from sklearn import ensemble
from sklearn import tree
from sklearn import model_selection

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("E:/Data Science/Data/")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.info()

X_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket', 'Name','Survived'], 1)
y_train = titanic_train['Survived']

dt = tree.DecisionTreeClassifier(random_state=2017) #1st is with Decissin Tree
rf = ensemble.RandomForestClassifier(random_state=2017) #2nd with Random Forest
adaboost = ensemble.AdaBoostClassifier(random_state=2017) #3rd one with Ada boost

#v_estimator1 = ensemble.VotingClassifier([('dt',dt), ('rf',rf)])
v_estimator1 = ensemble.VotingClassifier([('dt',dt), ('rf',rf), ('aboost',adaboost)])
model_selection.cross_val_score(v_estimator1, X_train, y_train, cv=10).mean()
v_estimator1.fit(X_train,y_train)

v_estimator2 = ensemble.VotingClassifier([('dt',dt), ('rf',rf), ('aboost',adaboost)], weights=[2,2,3], voting='soft')
cv_score = model_selection.cross_val_score(v_estimator2, X_train, y_train, cv=10)
type(cv_score) #numpy.ndarray
cv_score.mean()
v_estimator2.fit(X_train,y_train)