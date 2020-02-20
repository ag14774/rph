import torch
from rph import RandomProjectionHashModule

if __name__ == '__main__':
    s1 = "AAATGCGGATGT"
    s2 = "TAATGCGGATGT"
    d = {
        "AA": 0,
        "AC": 1,
        "AT": 2,
        "AG": 3,
        "CA": 4,
        "CC": 5,
        "CT": 6,
        "CG": 7,
        "TA": 8,
        "TC": 9,
        "TT": 10,
        "TG": 11,
        "GA": 12,
        "GC": 13,
        "GT": 14,
        "GG": 15
    }
    s1v = [0] * 16
    s2v = [0] * 16
    for i in range(len(s1) - 1):
        s1v[d[s1[i:i + 2]]] += 1
    for i in range(len(s2) - 1):
        s2v[d[s2[i:i + 2]]] += 1
    hash = RandomProjectionHashModule(16, 4)
    inp = torch.stack([torch.tensor(s1v), torch.tensor(s2v)])
    print(inp.size(), inp)
    print(hash(inp))
