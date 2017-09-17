import numpy as np
import nltk
from sklearn.externals import joblib
clf = joblib.load('RF.pkl')
count_vect = joblib.load('count_vect.pkl')
while(True):
	print("Enter statement:")
	new = count_vect.transform([raw_input()])
	print(clf.predict(new))
	if 0xFF == ord('q'): #Exit program when the user presses 'q'
		break
print("Thank you!!!")        