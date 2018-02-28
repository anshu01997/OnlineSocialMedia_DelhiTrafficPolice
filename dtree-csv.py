from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

try:
	#The classifier, here, attempts to read the 'tweet-class.csv' file
	#`header=None` means that the column names have not been given
	#`sep=','` means that the columns of the csv are separated by commas
	#`names=['tweets','class']` means that we have assigned names to the columns such that the first column represents
	# the tweets while the second column contains the corresponding class labels 
	df = pd.read_csv('tweet-class.csv', header=None, sep=',',names=['tweets', 'class'])   # columns names if no header
	
	#The TfidfVectorizer function transforms the input text into a feature vector
	#fit_transform() is used to learn the vocabulary dictionary and return term-document matrix
	vect = TfidfVectorizer()
	x = vect.fit_transform(df['tweets'].values.astype('U')) 
	y = df['class']
	
	#Setting parameters for the classifier.
	SIZE=50
	STEP=.02
	#Dividing the tweet-class.csv file into training and test dataset in the ratio of 85%:15%
	train,test,train_lab,test_lab=train_test_split(x,y,test_size=.15,random_state=100)
	clf=DecisionTreeClassifier()
	clf.fit(train,train_lab)
	#Running the classifier and printing the output labels for the rows in the test dataset, along with the
	#accuracy score
	output=clf.predict(test)
	print output
	print accuracy_score(test_lab,output)

except UnicodeDecodeError as e:
	print 'unicode error'
