#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import sys

import toolkit as tk


if __name__ == "__main__":
    try:
        assert len(sys.argv) > 1
    except AssertionError:
        print("Did not provide txt file with DNA sequence!")
    else:
        with open(sys.argv[1], "r") as f:
            sequences = []
            tmp = []
            while True:
                line = f.readline().rstrip()
                if line.startswith(">Rosalind"):
                    if tmp:
                        seq = "".join(tmp)
                        sequences.append(seq)
                        tmp = []
                else:
                    tmp.append(line.strip())
                if not line:
                    sequences.append("".join(tmp))
                    break

        for seq in sequences[:2]:
            for other_seq in sequences:
                print(other_seq, seq)
                if other_seq == seq:
                    continue
                n = 0
                substr = ""
                ret = []
                while n < len(seq) and n < len(other_seq):
                    if other_seq[n] == seq[n]:
                        substr += other_seq[n]
                    if substr != "" and other_seq[n] != seq[n]:
                        ret.append(substr)
                        substr = ""
                    n += 1
                ret.append(substr)
                print(ret)
