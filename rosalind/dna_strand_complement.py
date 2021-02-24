"""Solves Rosalind problem 'Complementing a Strand of DNA'"""
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
            data = f.readlines().pop().rstrip()
            print(tk.reverse_complement(data))
