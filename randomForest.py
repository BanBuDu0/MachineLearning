import csv
import random
from sklearn.ensemble import RandomForestClassifier

data = [ i for i in csv.reader(file('wine.data', 'rb')) ]
random.shuffle(data)

X = [ i[1:] for i in data ]
Y = [ i[0] for i in data ]

train_cutoff = len(data) * 3/4

X_train = X[:train_cutoff]
Y_train = Y[:train_cutoff]
X_test = X[train_cutoff:]
Y_test = Y[train_cutoff:]

classifier = RandomForestClassifier(n_estimators=10)
classifier = classifier.fit(X_train, Y_train)

Y_predict = classifier.predict(X_test)

equal = 0
z