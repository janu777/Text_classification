import numpy as np
import nltk
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
labelled_file = open('questions.txt')
train_data = labelled_file.readlines()
np.random.shuffle(train_data)
X_data = []
y_data = []
for x in train_data:
	nltk.word_tokenize(x)
	y_data.append((nltk.word_tokenize(x))[-1]) 
	X_data.append(x.rsplit(' ', 2)[0])
X_train = X_data[:1300]
y_train = y_data[:1300]
X_test = X_data[1300:]
y_test = y_data[1300:]		
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
clf1 = RandomForestClassifier(n_estimators=2000).fit(X_train_counts, y_train)
predict_train = clf1.predict(X_train_counts)
X_test_counts = count_vect.transform(X_test)
predict_test = clf1.predict(X_test_counts)
print(np.mean(predict_train == y_train))
print(np.mean(predict_test == y_test))
X_data_counts = count_vect.fit_transform(X_data)
clf2 = RandomForestClassifier(n_estimators=2000).fit(X_data_counts, y_data)
joblib.dump(clf2, 'RF.pkl') 
joblib.dump(count_vect, 'count_vect.pkl') 