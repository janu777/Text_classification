# Text_classification
Identify Question Type: Given a question, the aim is to identify the category it belongs to. 

The four categories used are : Who, What, When, Affirmation(yes/no). 

Label any sentence that does not fall in any of the above four as "Unknown" type.

# Model:
The model was trained using Random Forest Classifier.

Accuracy:

Training_accuracy: 100%

Testing_accuracy: 97%

# Dependencies:

sklearn

nlkt

numpy

# Execution:

python test.py

# Output:

Enter statement:

When will you go to school?

['when']

Enter statement:

What is the time now?

['what']

Enter statement:

who is the father of our nation?

['who']

Enter statement:

Is it going to rain?

['affirmation']

Enter statement:

How are you? 

['unknown']
