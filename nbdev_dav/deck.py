# AUTOGENERATED! DO NOT EDIT! File to edit: ..\01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ..\01_deck.ipynb 2
from .card import *
from fastcore.utils import *
import random

# %% ..\01_deck.ipynb 4
class Deck:
    "A deck of 52 cards"
    def __init__(self):
        self.cards = [Card(s,r) for s in range(4) for r in range(1,14)]
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return'; '.join(map(str, self.cards))
    def __contains__(self, card):
        return card in self.cards
    __repr__=__str__
    
    def shuffle(self):
        "Shuffles the cards in this deck"
        random.shuffle(self.cards)

# %% ..\01_deck.ipynb 10
@patch
def pop(self:Deck,
        idx:int=-1):
    "Remove one card from the deck, defaulting to the last index"
    return self.cards.pop(idx)

# %% ..\01_deck.ipynb 12
@patch
def remove(self:Deck,
        card:Card):
    "Removes specified card from the deck"
    return self.cards.remove(card)

# %% ..\01_deck.ipynb 13
@patch
def draw_n(n:int,
           replace:bool=True):
    "Draws n cards, with replacement if replace"
    d = Deck()
    d.shuffle()
    if repalce: return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else: return d.cards[:n]
