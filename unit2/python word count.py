# coding=utf-8

file = './unit2/readme.md'

text = open(file).read()
# 读取文件

char_list = [',', '.', '!', '?', '\n', '\t', '\"', '\'']
# 单词间分割符列表

for each_char in char_list:
    text = text.replace(each_char, ' ')
# 将char_list中的符号全部替换为空格

words = text.split()

# 以空格为界，分割拆分文本。保存为list

print('Word count:\t', len(words))
