
a = ord('a')
alphabet = "".join(chr(a+x) for x in range(26)) + "æøå"
del a

class Spejd:
    def __init__(self, codeword):
        self.codeword = codeword
        self.shifted = codeword + "".join( c for c in alphabet if c not in codeword)

    def encode_char(self, c:str):
        lc = c.lower()
        if lc in alphabet:
            inx = alphabet.index(lc)
            lcc = self.shifted[inx]
            return lcc if c.islower() else lcc.upper()
        else:
            return c

    def encode(self, s:str) -> str:
        return ''.join(map(self.encode_char, s))

    def alphabets(self):
        return alphabet, self.shifted
