import numpy as np
import tensorflow
import tflearn
import random
import json
import chatbot
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

with open("chatbot.json") as file:
    data = json.load(file)

print(data)