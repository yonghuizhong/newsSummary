from Summary import TextRankSentence

text = open('news.txt', encoding='UTF-8', errors='ignore').read()
title = open('news_title.txt', encoding='UTF-8', errors='ignore').read()
# print(text)
textrank = TextRankSentence.TextRankSentence()
textrank.analyze(text=text, title=title)  # 得到排序后的句子
summary = textrank.get_key_sentences(num=2)
print(summary)
