import nltk
from nltk.corpus import stopwords
import re
from nltk.sentiment import SentimentIntensityAnalyzer

# Loading the book
with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    book = file.read()

# Taking all words in the book
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

# Count how much each words is used in the book
d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

# Convert to list and sort it descending
d_list = [(value, key) for key, value in d.items()]
d_list.sort(reverse=True)

# Taking english stopwords
english_words = stopwords.words("english")

# Filtering out stopwords
filtered_words = []
for count, word in d_list:
    if word not in english_words:
        filtered_words.append((word, count))

# Using Sentiment Intensity Analyzer and Polarity Scores for first time
analyzer = SentimentIntensityAnalyzer()
sample_positive_text = "Hello, I love this beautiful town. I just love them"
scores = analyzer.polarity_scores(sample_positive_text)
sample_negative_text = "Hello, I hate this vicious town. I just hate them"
scores = analyzer.polarity_scores(sample_negative_text)

# Mood of the book
scores = analyzer.polarity_scores(book)

# Mood of the individual chapters
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]
for index, chapter in enumerate(chapters):
    scores = analyzer.polarity_scores(chapter)
    print(index+1, scores)