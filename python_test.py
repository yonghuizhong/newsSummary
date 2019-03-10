# 测试：使用正则表达式划分文章
import re
from Summary import tool

text = open('news.txt', encoding='UTF-8', errors='ignore').read()
regex_pattern = '|'.join(map(re.escape, tool.sentence_delimiters))
sentences = re.split(regex_pattern, text)
print(len(sentences))
sentences = [i.strip() for i in sentences if len(i.strip()) > 0]
print(len(sentences), sentences)
