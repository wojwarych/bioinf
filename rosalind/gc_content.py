"""Solves Rosalind problem 'Computing GC Content'"""
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
        ret = []
        tmp = []
        with open(sys.argv[1], "r") as f:
            while True:
                line = f.readline()
                if line.startswith(">Rosalind"):
                    if tmp:
                        seq = "".join(tmp)
                        ret.append((name, seq))
                        tmp = []
                    name = line.rstrip().lstrip(">")
                else:
                    tmp.append(line.rstrip())
                if not line:
                    ret.append((name, "".join(tmp)))
                    break
        gc_content = [(name, tk.gc_content(seq)) for (name, seq) in ret]
        max_prot = max(gc_content, key=lambda item: item[1])
        print("{}\n{:.6f}%".format(*max_prot))
