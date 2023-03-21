
alphabet = """
a *-
b -***
c -*-*
d -**
e *
f **-*
g --*
h ****
i **
j *---
k -*-
l *-**
m --
n -*
o ---
p *--*
q --*-
r *-*
s ***
t -
u **-
v ***-
w *--
x -**-
y -*--
z --**
æ *-*-
ø ---*
å *--*-"""


dash = '‒'
dash = '-'
dot = '·'

alphabet = alphabet.replace('-', dash).replace('*', dot)
alphabet = alphabet.strip().splitlines()
alphabet = map(str.split, alphabet)
alphabet = dict(alphabet)


def encode_word(word:str) -> str:
    symbols = map(alphabet.get, word.lower())
    return '/'.join(symbols)

def MorseEncode(s:str) -> str:
    s = s.split()
    words = map(encode_word, s)
    sentence = '//'.join(words)
    return f"///{sentence}///"
    
