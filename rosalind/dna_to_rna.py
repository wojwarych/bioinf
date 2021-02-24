"""Solves Rosalind problem called 'Transcribing DNA to RNA'"""
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import sys

import toolkit as tk


if __name__ == "__main__":
    try:
        assert len(sys.argv) > 1
    except AssertionError:
        print("No txt file provided!")
    else:
        with open(sys.argv[1], "r") as f:
            data = f.readlines().pop().rstrip()
            print(tk.transcript(data))
