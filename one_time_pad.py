# M = {0, 1}^n
# K = {0, 1}^n

# Ek(m) = C0, C1, ..........., C(n-1)
# where Ci = Mi xor Ki

# converts ord(<one char string>) -> decimal no. -> bits
# does XOR with each and every bit of the CIPHER


def convert_to_bits(n, pad):
    result = []
    while n>0:
        if n % 2 == 0:
                result = [0] +result
        else
                result = [1] + result
        n = n / 2 # coverts a character in to equivalent ascii to bits
        while len(result) < pad:
            result = [0] + result
        return result #

def string_to_bits(s):
    result = []
    for c in s:
        result = convert_to_bits(ord(c), 7) + result # If 67, 7 then returns [1,0,0,0,0,1,1]
    return result # & if ('CS') then returns [1,0,1,0,0,1,1,1,0,0,0,0,1,1]

def bits_to_char(b):
    assert len(b) == 7