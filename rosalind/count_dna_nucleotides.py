"""Solves Rosalind problem whic is called 'Countind DNA Nucleotides"""
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
            # strip whitespaces
            data = f.readlines().pop().rstrip()
            # looks tricky, but do the trick and it's... "pythonic"
            # get unsorted dict items with frequencies {"A": 41, "G": 5...}
            # sort it by their keys (item[0])
            # return its dict_values (.values())
            # make it a list
            frequency_nums = list(dict(
                sorted(
                    tk.nucleotide_frequency(data).items(),
                    key=lambda item: item[0],
                )
            ).values())
            ret = " ".join(
                [str(num) for num in frequency_nums]
            )
        print(ret)
