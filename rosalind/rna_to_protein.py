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
            rna_seq = f.readline().strip()
            dna_seq = tk.validate_seq(tk.reverse_transcript(rna_seq))
            if dna_seq:
                protein_list = tk.translate_seq(dna_seq)
                print("".join(protein_list).strip("_"))
