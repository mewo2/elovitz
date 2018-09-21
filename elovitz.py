# -*- coding: utf-8 -*-

from collections import namedtuple
import re

re_patterns = {
    '^': r'[bcdfghjklmnpqrstvwxz]',
    '#': r'[aeiouy]+',
    '+': r'[eiy]',
    ':': r'[bcdfghjklmnpqrstvwxz]*',
    '*': r'[bcdfghjklmnpqrstvwxz]+',
    '.': r'[bdvgjlmnrwz]',
    '$': r'[bcdfghjklmnpqrstvwxz][ei]',
    '%': r'(er|e|es|ed|ing|ely)',
    '&': r'(ch|sh|[scgzxj])',
    '@': r'(th|ch|sh|[tsrdlznj])'
}

ipa_chars = {
    'iy': 'iː',
    'ih': 'ɪ',
    'ey': 'eɪ',
    'eh': 'ɛ',
    'ae': 'æ',
    'aa': 'ɑː',
    'ao': 'ɔː',
    'ow': 'oʊ',
    'uh': 'ʊ',
    'uw': 'uː',
    'er': 'ɜːr',
    'ax': 'ə',
    'ah': 'ʌ',
    'ay': 'aɪ',
    'aw': 'aʊ',
    'oy': 'ɔɪ',
    'p': 'p',
    'b': 'b',
    't': 't',
    'd': 'd',
    'k': 'k',
    'g': 'g',
    'f': 'f',
    'v': 'v',
    'th': 'θ',
    'dh': 'ð',
    's': 's',
    'z': 'z',
    'sh': 'ʃ',
    'zh': 'ʒ',
    'hh': 'h',
    'm': 'm',
    'n': 'n',
    'nx': 'ŋ',
    'l': 'l',
    'w': 'w',
    'y': 'j',
    'r': 'r',
    'ch': 't͡ʃ',
    'jh': 'd͡ʒ',
    'wh': 'ʍ'
}

def re_pattern(pattern, final=False):
    r = ''
    for p in pattern:
        assert p.isalpha() or p in re_patterns or p in " '", p
        r += re_patterns.get(p, p)
    if final:
        r += '$'
    return re.compile(r)

class Rule(namedtuple("Rule", "pre srcpost src dst")):
    def matches(self, word, pos):
        return self.pre.search(word[:pos]) and self.srcpost.match(word[pos:])

def load_rule(line):
    pre, rest = line.split('[')
    src, rest = rest.split(']')
    post, rest = rest.split('=')
    dst = rest.split('/')[1]
    return Rule(re_pattern(pre, True), re_pattern(src + post), src, dst.split())

rules = [load_rule(line) for line in open("rules.txt") if line.strip()]


def pronounce(word):
    word = ' ' + word.lower() + ' '
    pron = []
    pos = 0
    while pos < len(word):
        for rule in rules:
            if rule.matches(word, pos):
                pron.extend(rule.dst)
                pos += len(rule.src)
                break
        else:
            raise NotImplementedException("No rule for %s:%d" % (word[1:-1], pos))
    return pron

def ipa(word):
    return ''.join(ipa_chars[phon] for phon in pronounce(word))
