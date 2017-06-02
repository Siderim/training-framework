https://siderim.github.io/training_framework/



## Welcom to Training-Framework





```markdown

                    *ML Text Classifier README* 
              ____________________________________________

NAME:
    ML Text Classifier
    
AUTHORS:
    Michael Siderius
    Rimika Majumdar
    
LAST MODIFIED:
    May 31, 2017
    
SYNOPSIS:
    
    This ML Text Classifier is being developed to create an optimized harassment detection.
    With the increasing growth of social media, it is inevitable that the levels of abusive language rise substantially.Thus,
    detection of abusive language has become an issue of increasing importance. That motivates our project. 
    
    
INVOCATION:
 
     To invoke the program, it requres specific flags. There is one required flag and 3 optional flags.
     
     You must specify the model to be used using the '-m' flag. 
              @ Multipolynomial Naive Bayes:            "python framekwork.py -m nb" 
              @ Support Vector Machine:                 "python framekwork.py -m svm" 
              @ Random Forest:                          "python framekwork.py -m rf"
              @ Decision Tree:                          "python framekwork.py -m dt"
              @ Multi-layer Perceptron Neural Network:  "python framekwork.py -m nn"
              
      To use a custom train set:
              @ Custom Train Set:                       "python framekwork.py -m svm -tr customTrain.csv"
      
      To use a custom test set:
              @ Custom Test Set:                        "python framekwork.py -m svm -te customTest.csv"
      
      To output the resulting predictions:
              @ Output CSV file:                        "python framekwork.py -o output.csv -m svm -te customTest.csv"
              
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
    
 
