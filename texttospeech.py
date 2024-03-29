# -*- coding: utf-8 -*-
"""texttospeech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NHYLZnAp6bGsZ4DJy7j7wW6YiAspMWwc
"""
#Install Packages
!pip install nltk gTTS newspaper3k

#Imports
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get Article
article = Article('https://www.cbc.ca/sports/basketball/nba/toronto-raptors-dallas-mavericks-recap-dec-22-1.5406336')

article.download() #Download The Article
article.parse() #PArse The Article
nltk.download('punkt') #Download Package
article.nlp() #Apply NLP (Natural Language Processing)

#Get The Articles Text And Store It Into A Variable Called 'mytext'
mytext = article.text

#Print The Text
print(mytext)

language = 'en' #English
#Convert Text To Speech
myobj = gTTS(text=mytext, lang=language, slow=False)
#Save Converted Audio To A File
myobj.save('read_article.mp3')
#Play Converted FIle
os.system('start read_article.mp3')
