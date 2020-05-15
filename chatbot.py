import numpy as np
import tensorflow
import tflearn
from nltk.stem.lancaster import LancasterStemmer
import random
import json
import chatbot


stemmer = LancasterStemmer()

with open("chatbot.json") as file:
    data = json.load(file)

print(data)