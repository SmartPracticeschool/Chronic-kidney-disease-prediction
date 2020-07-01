import glob
from keras.models import Sequential, load_model
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import matplotlib.pylot as pylot


#loading the data from the data-set
from google.colab import files
uploaded= files.upload()

df= pf.read_csv('kidney_disease.csv')

