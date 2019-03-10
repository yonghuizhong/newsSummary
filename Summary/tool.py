import math
import numpy as np
import networkx as nx

sentence_delimiters = ['…', '……', '?', '!', ';', '？', '！', '；', '。', '\n']
allow_speech_tags = ['an', 'i', 'j', 'l', 'n', 'nr', 'nrfg', 'ns', 'nt', 'nz', 't', 'v', 'vd', 'vn', 'eng']


class AttrDict(dict):
    """Dict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


# 两个句子的相似度
def similarity(word_list1, word_list2):
    words = list(set(word_list1 + word_list2))
    list1 = [float(word_list1.count(w)) for w in words]  # 每个词在句子1出现的次数
    list2 = [float(word_list2.count(w)) for w in words]

    list3 = [list1[i] * list2[i] for i in range(len(list1))]
    list4 = [1 for i in list3 if i > 0]  # 每个词如果均在两个句子中出现，则为1
    all_num = sum(list4)

    if abs(all_num) <= 1e-12:
        return 0

    denominator = math.log(float(len(word_list1)) + float(len(word_list2)))  # 分母
    if abs(denominator) < 1e-12:
        return 0

    return all_num / denominator


# 根据pr值将句子按关键程度从大到小排序，添加了权值
# sentences: 列表，元素为句子
# words: 二维列表，子列表与sentences列表的元素对应，子列表由对应句子的单词构成
# sim_function: 计算两个句子的相似度，作为句子的权值
def sort_sentences(sentences, words, sim_function=similarity):
    num = len(sentences)
    graph = np.zeros((num, num))  # 生成num行num列的零矩阵

    for x in range(num):
        for y in range(x, num):
            sim_value = sim_function(words[x], words[y])  # 句子x与句子y的相似度，即权值
            graph[x, y] = sim_value  # 无向有权图
            graph[y, x] = sim_value

    nx_graph = nx.from_numpy_matrix(graph)  # 从上面的矩阵中得到图
    scores = nx.pagerank(nx_graph)  # 返回pr值，字典类型：key为索引，value为分数
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)  # 按分数进行降序输出，列表类型
    sorted_sentences = []
    for index, score in sorted_scores:  # 列表元素为(index, score)
        item = AttrDict(index=index, sentence=sentences[index], weight=score)
        sorted_sentences.append(item)  # 列表元素为字典格式
    return sorted_sentences


if __name__ == '__main__':
    pass
