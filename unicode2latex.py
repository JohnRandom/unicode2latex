#-*- coding: utf8 -*-
import sys


MAP = {
    '\\l': 'ł',
    '\\`{o}': 'ò',
    '\\'{o}': 'ó',
    '\\^{o}': 'ô',
    '\\"{o}': 'ö',
    '\\H{o}': 'ő',
    '\\~{o}': 'õ',
    '\\c{c}': 'ç',
    '\\k{a}': 'ą',
    '\\={o}': 'ō',
    '\\b{o}': 'o',
    '\\.{o}': 'ȯ',
    '\\d{u}': 'u',
    '\\r{a}': 'å',
    '\\u{o}': 'ŏ',
    '\\v{s}': 'š',
    '\\t{oo}': 'o͡o'
}


def unicode2latex(text):
    for key, value in MAP.iteritems():
        text = text.gsub(value, key)


if __name__ == '__main__':
    tex_file = open(sys.argv[1])
    text = tex_file.readlines()
    tex_file.close()

    print unicode2latex(text)
