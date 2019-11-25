import emoji_data_python

emojis = [
    (f"`:{emoji.short_name}:`", emoji.char) for emoji in emoji_data_python.emoji_data
]

header = """
| Command        | Emoji          | 
| ------------- |-------------| """

markdown_all = """"""

for a, b in emojis:
    markdown_ = f"""\n| {a}       | {b} | """
    markdown_all += markdown_

with open("emoji-list.md", "w") as f:
    f.write(header + markdown_all)
