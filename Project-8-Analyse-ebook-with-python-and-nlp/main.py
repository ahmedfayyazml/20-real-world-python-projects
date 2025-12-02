with open("miracle_in_the_andes.txt") as file:
    book = file.read()

## Finding the number of the chapter

import  re
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern,book)
chapters = chapters[1:]

## Finding the chapters of the book that are negative and positive

from nltk.sentiment import  SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

## running loop to find

for nr,chapter in enumerate(chapters):
    score = analyzer.polarity_scores(chapter)
    if score['pos']>score['neg']:
        print(nr,"Positive")
    else:
        print(nr,"Positive")
