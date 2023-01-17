import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wiki = wikipedia.page('Artificial Intelligence')

text = wiki.content

wordcloud = WordCloud(width = 2000, height = 1500).generate(text)
plt.figure(figsize=(10, 9))
plt.title('Artificial Intelligence')
plt.xlabel('width')
plt.ylabel('height')

plt.imshow(wordcloud)

plt.show()