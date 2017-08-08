
                    *ML Text Classifier README* 
              ____________________________________________

NAME:
    ML Text Classifier
    
    
LAST MODIFIED:
    May 31, 2017
    
SYNOPSIS:
    
    This ML Text Classifier is being developed to create an optimized harassment detection.
    With the increasing growth of social media, it is inevitable that the levels of abusive language rise substantially.Thus,
    detection of abusive language has become an issue of increasing importance. That motivates our project. 
    
    
INVOCATION:
 
     To invoke the program, it requres specific flags. There is one required flag and 3 optional flags.
     
     You must specify the model to be used using the '-m' flag. 
              @ Multipolynomial Naive Bayes:            "python framework.py -m nb" 
              @ Support Vector Machine:                 "python framework.py -m svm" 
              @ Random Forest:                          "python framework.py -m rf"
              @ Decision Tree:                          "python framework.py -m dt"
              @ Multi-layer Perceptron Neural Network:  "python framework.py -m nn"
              
      To use a custom train set:
              @ Custom Train Set:                       "python framework.py -m svm -tr customTrain.csv"
      
      To use a custom test set:
              @ Custom Test Set:                        "python framework.py -m svm -te customTest.csv"
      
      To output the resulting predictions:
              @ Output CSV file:                        "python framework.py -o output.csv -m svm -te customTest.csv"
              
      Note: Flag order does not matter
 
 DATA SETS: 
       Please note that the format of the data must be constant if using a custom dataset. 
       The format is as respectively such within the csv...
       
       C1, C2
       Comment, Label
 
 
 DEPENDENCIES:
      python 2.7
      
      import re
      import sys
      import numpy
      import scipy
      import nltk
      import pandas
      import csv
      import sklearn
    
 
 
https://siderim.github.io/training_framework/
