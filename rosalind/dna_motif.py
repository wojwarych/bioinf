"""Solves Rosalind problem 'Finding a Motif in DNA'"""
#!/user/bin/env python3
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
            str_input = f.readline().strip()
            sub_str = f.readline().strip()
            idx = 0
            ret = []
            while idx < len(str_input):
                try:
                    if str_input[idx:len(sub_str)+idx] == sub_str:
                        ret.append(idx+1)
                except IndexError:
                    break
                idx += 1
        print(" ".join(map(str, ret)))
