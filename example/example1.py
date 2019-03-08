from Summary import TextRankSentence

text = open('news.txt').read()
# print(text)
textrank = TextRankSentence.TextRankSentence()
textrank.analyze(text=text)  # 得到排序后的句子
summary_list = textrank.get_key_sentences(num=3)
for i in summary_list:
    print(i.index, i.weight, i.sentence)
