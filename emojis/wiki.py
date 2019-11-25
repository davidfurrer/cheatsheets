import wikipedia
import emoji_data_python

emojis = [
    emoji.short_name for emoji in emoji_data_python.emoji_data
]
#print(emojis)

text = wikipedia.summary("Moon", sentences=5)

d=[x if x.lower() not in emojis else f':{x.lower()}:' for x in text.split(' ')]
s=' '.join(d)

with open("wiki.md", "w") as f:
    f.write(s)