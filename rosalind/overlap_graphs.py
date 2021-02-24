#!/user/bin/env python3
#! -*- coding: utf-8 -*-
import itertools
import sys

import toolkit as tk


if __name__ == "__main__":
    try:
        assert len(sys.argv) > 1
    except AssertionError:
        print("Did not provide txt file with DNA sequence!")
    else:
        with open(sys.argv[1], "r") as f:
            sequences = dict()
            tmp = []
            while True:
                line = f.readline().rstrip()
                if line.startswith(">Rosalind"):
                    if tmp:
                        seq = "".join(tmp)
                        sequences[name] = seq
                        tmp = []
                    name = line.strip(">")
                    sequences[name] = ""
                else:
                    tmp.append(line.strip())
                if not line:
                    sequences[name] = "".join(tmp)
                    break
    ret = []
    for v, u in itertools.combinations(sequences, 2):
        if sequences[v][-3:] == sequences[u][:3]:
            ret.append((v, u))

        if sequences[u][-3:] == sequences[v][:3]:
            ret.append((u, v))

    for out in ret:
        print(out[0], out[1])
