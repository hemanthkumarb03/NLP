import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
messages = pd.read_csv("D:\NLP\NLP_FROM_BASICS\Spam Classification\data\SMSSpamCollection",sep='\t',names=['label','messages'])
