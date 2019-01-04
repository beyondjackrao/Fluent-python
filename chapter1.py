# -*- coding:utf-8 -*-
import collections
from random import choice
# 用来构建一些只有少数属性没有方法的类
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    #len()会调用类的__len__方法
    print(len(deck))
    #deck[]会调用__getitem__方法
    print(deck[0])
    print(deck[-1])
    print(choice(deck))
    print(deck[:3])
    print(deck[12::13])