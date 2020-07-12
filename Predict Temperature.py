import math
import os
import random
import re
import sys

#
# Complete the 'predictTemperature' function below.
#
# The function is expected to return a FLOAT_ARRAY.
# The function accepts following parameters:
#  1. STRING startDate
#  2. STRING endDate
#  3. FLOAT_ARRAY temperature
#  4. INTEGER n
#
import sklearn

import datetime
from datetime import date
from datetime import timedelta
from sklearn import ensemble
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
# from xgboost import XGBClassifier
from sklearn.feature_extraction.text import CountVectorizer


def timestamp(argdate, number_days):
    add_hour = timedelta(hours = 1)
    timelist = []
    for i in range(24*number_days):
        timelist.append(argdate.strftime("%Y-%m-%d %H:%M"))
        argdate += add_hour

    return timelist

def predictTemperature(startDate, endDate, temperature, n):
    # Write your code here
    add_hour = timedelta(hours = 1)
    firstdatepart = startDate.split()
    date1 = firstdatepart[0].split('-')
    # date2 = firstdatepart[1].split(':')

    d1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]), 00, 00)
    initial_date = date(int(date1[0]), int(date1[1]), int(date1[2]))

    seconddatepart = endDate.split()
    date3 = seconddatepart[0].split('-')
    # date4 = seconddatepart[1].split(':')

    d2 = datetime.datetime(int(date3[0]), int(date3[1]),int(date3[2]), 23, 00)

    final_date = date(int(date3[0]), int(date3[1]), int(date3[2]))

    number_days = (final_date - initial_date).days
    # print(number_days)
    x = timestamp(d1, number_days + 1)

    vector = CountVectorizer()
    X = vector.fit_transform(x)

    machine_learn = ensemble.GradientBoostingRegressor()
     # machine_learn = LogisticRegression()
    # machine_learn = Rand#omForestClassifier (n_estimators = 10)
    # machine_learn = XGBClassifier()
    machine_learn.fit(X, temperature)

    prediction_date = timestamp(d2 + add_hour, n)
    y_data = vector.transform(prediction_date)
    y = list(machine_learn.predict(y_data))

    return y

startDate = "2019-01-01 00:00"
endDate = "2019-01-05 01:00"
n = 1
temperature = [3,4,5,6,5,4,5,7,8,9,3,4,5,6,5,4,5,7,8,9,10,12,8,7,3,4,5,6,5,4,5,7,8,9,3,4,5,6,5,4,5,7,8,9,10,12,8,7,3,4,5,6,5,4,5,7,8,9,3,4,5,6,5,4,5,7,8,9,10,12,8,7]

print(predictTemperature(startDate, endDate, temperature, n))

