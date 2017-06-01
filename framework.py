#
# @author: Michael Siderius
# @desc: Framework for text classification.  
# @lang: Python2.7
#
# @flags: -o $output.csv, -m $model , -tr $trainingSet.csv , -te $testingSet.csv
#

import re
import sys
import nltk
import pandas as pd
import preprocess as pre
import csv


from sklearn.neural_network import MLPClassifier
from sklearn import svm, naive_bayes, tree
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.metrics import classification_report

tfidf_vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('english'),  strip_accents='ascii')
write_to_csv = True


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def extract_features(docs):
	docs = map(pre.preprocess_text, docs)
	features = tfidf_vectorizer.fit_transform(docs)
	return features

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def train_svm(data):
	X = extract_features(row[0] for row in data)
	x = [row[1] for row in data]
	clf = svm.SVC(kernel='linear', probability=True)
	clf.fit(X, x)
	return clf

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def train_nb(data):
	X = extract_features(row[0] for row in data)
	x = [row[1] for row in data]
	nb = naive_bayes.MultinomialNB()
	nb.fit(X,x)
	return nb

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def train_rf(data):
	X = extract_features(row[0] for row in data)
	x = [row[1] for row in data]
	rfc = RFC(n_estimators = 100, oob_score = True, max_features = ("auto"))
	rfc.fit(X, x)
	return rfc 


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def train_dt(data):
	X = extract_features(row[0] for row in data)
	x = [row[1] for row in data]
	dt = tree.DecisionTreeClassifier()
	dt = dt.fit(X, x)
	return dt 


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def train_nn(data):
	X = extract_features(row[0] for row in data)
	x = [row[1] for row in data]
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
	clf = clf.fit(X, x)
	return clf 


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def fetch_args(args):
	train_set = "default"
	test_set = "default"
	output = False
	
	if "-m" in args:
		classification = args[args.index("-m") + 1]
	else:
		print("No training method detected, see manual.")
		sys.exit(1)
	
	if "-tr" in args:
		train_set = args[args.index("-tr") + 1]
	if "-te" in args:
		test_set = args[args.index("-te") + 1]

	if "-o" in args:
		output = args[args.index("-o") + 1]

	return classification, train_set, test_set, output


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def predict(clf,test_data):
	y_true = [row[1] for row in test_data]
	docs = map(pre.preprocess_text, [row[0] for row in test_data])
	tfidf = tfidf_vectorizer.transform(docs)
	y_pred = clf.predict(tfidf)

	return y_pred, y_true


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def build_classification_report(y_pred, y_true):
	report = classification_report(y_true, y_pred)
	return report

# @method: fetch_args()
# @param: sys arguments
# @desc: 
#

def cross_validation_report(clf, dataset):
	data = tfidf_vectorizer.transform([row[0] for row in dataset])
	target = [row[1] for row in dataset]
	return cross_validation.cross_val_score(clf, data, target)


# @method: fetch_args()
# @param: sys arguments
# @desc: 
#
def output_results(entry,y_pred,output):

	csv_out = open(output, 'wb')
	mywriter = csv.writer(csv_out)

	rows = zip(entry,y_pred)
	mywriter.writerows(rows)
	csv_out.close()


if __name__ == '__main__':
	classification, train_set, test_set, output = fetch_args(sys.argv)

	if train_set == 'default': train_data = 'train.csv'
	else: train_data = train_set
	
	if test_set == 'default': test_data = 'test.csv'
	else: test_data = test_set

	train_data = pd.read_csv(train_data, encoding='utf8').as_matrix()
	test_data = pd.read_csv(test_data, encoding = 'utf8').as_matrix()

	if classification == "nb":
		clf = train_nb(train_data)

	elif classification == "svm":
		clf = train_svm(train_data)

	elif classification == "rf":
		clf = train_rf(train_data)

	elif classification == "dt":
		clf = train_dt(train_data)

	elif classification == "nn":
		clf = train_dt(train_data)

	else:
		print("Method not defined")
		sys.exit(1)
	
	y_pred, y_true = predict(clf,test_data)
	print(build_classification_report(y_pred,y_true))

	if output != False:
		output_results(test_data, y_pred, output)











