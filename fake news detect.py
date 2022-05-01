import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

#Read the data 
df=pd.read_csv('C:\Users\patil\OneDrive\Desktop\news.csv')

#Get shape and head
df.shape
df.head()

#Get shape and head
df.shape
df.head()