#!/usr/bin/env python


def count_char(word):
    char_dic = {}
    for letter in word:
        char_dic[letter] = char_dic.get(letter, 0) + 1
    return char_dic

print(count_char('banana'))
