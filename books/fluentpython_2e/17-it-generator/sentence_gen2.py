"""
Sentence: iterate over words using a generator function
"""

# tag::SENTENCE_GEN2[]
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text  # 不再需要 words 列表

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):  # finditer 函数构建一个迭代器，包含 self.text 中匹配 RE_WORD 的单词，产出 MatchObject 实例
            yield match.group()  # 从 MatchObject 实例中提取匹配的文本

# end::SENTENCE_GEN2[]
