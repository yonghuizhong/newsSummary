from . import tool
from .Segmentation import Segmentation


class TextRankSentence(object):
    def __init__(self):
        self.seg = Segmentation()
        self.sentences = None
        self.words = None
        self.key_sentences = None

    def analyze(self, text):
        self.key_sentences = []
        result = self.seg.segment(text=text)  # 得到分词后的结果
        self.sentences = result.sentences  # 句子列表
        self.words = result.words  # 二维列表

        # 得到排序后的句子，列表元素包含索引、句子、权重（即PR值）
        self.key_sentences = tool.sort_sentences(sentences=self.sentences,
                                                 words=self.words)

    # 生成摘要：最重要的num个句子长度>=min_len的句子
    def get_key_sentences(self, num=6, min_len=6):
        result = []
        count = 0
        for i in self.key_sentences:
            if count >= num:
                break
            if len(i['sentence']) >= min_len:
                result.append(i)
                count += 1
        return result


if __name__ == '__main__':
    pass
