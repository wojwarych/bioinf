"""Solves Rosalind problem 'Counting Point Mutations'"""
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
            while True:
                line_1 = f.readline().strip()
                line_2 = f.readline().strip()
                if not line_2:
                    break
                count = 0
                for nuc_1, nuc_2 in zip(line_1, line_2):
                    if nuc_1 != nuc_2:
                        count += 1
        print(count)
