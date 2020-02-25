# coding=utf-8


def word_count(filename):
    import os.path
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            text = file.read()
            char_list = [
                ',', '.', ';', ':', '(', ')', '!', '?', '\n', '\t', ' \"',
                ' \'', '/', '\\'
            ]
            # 单词间分割符列表

            for each_char in char_list:
                text = text.replace(each_char, ' ')
            # 将char_list中的符号全部替换为空格

            words = text.split()
            # 以空格为界，分割拆分文本。保存为list
            words_num = len(words)

    return words_num


file = './unit2/readme.md'

word_num = word_count(file)

print('word numbers', word_num)
