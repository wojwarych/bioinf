#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import random
from typing import List, Union

from .structures import DNA_CODONS, DNA_REVERSE_COMPLEMENT, NUCLEOTIDES


def validate_seq(dna_seq: str) -> Union[str, bool]:
    dna_seq = dna_seq.upper()
    for nuc in dna_seq:
        if nuc not in NUCLEOTIDES:
            print(nuc)
            return False
    return dna_seq


def nucleotide_frequency(dna_seq: str) -> Union[dict, None]:
    try:
        return {nuc: dna_seq.count(nuc) for nuc in dna_seq}
    except TypeError:
        return None


def transcript(dna_seq: str) -> str:
    return dna_seq.replace("T", "U")


def reverse_transcript(rna_seq: str) -> str:
    return rna_seq.replace("U", "T")


def reverse_complement(dna_seq) -> str:
    return "".join([DNA_REVERSE_COMPLEMENT[nuc] for nuc in dna_seq])[::-1]


def gc_content(dna_seq) -> float:
    return round(
        (dna_seq.count("C") + dna_seq.count("G")) / len(dna_seq) * 100,
        6
    )


def gc_content_in_seq(dna_seq, k) -> List[int]:
    return [gc_content(dna_seq[pos:pos+k]) for pos in range(0, len(dna_seq), k)]


def translate_seq(dna_seq, init_pos=0) -> List[str]:
    return [
        DNA_CODONS[dna_seq[pos:pos+3]]
        for pos
        in range(init_pos, len(dna_seq) - 2, 3)
    ]

def codon_usage(dna_seq, aminoacid) -> dict:
    tmp_list = [
        dna_seq[i:i +3]
        for i in range(0, len(dna_seq) - 2, 3)
        if DNA_CODONS[dna_seq[i:i +3]] == aminoacid
    ]
    freq_dict = {codon: tmp_list.count(codon) for codon in tmp_list}
    total_weight = sum(freq_dict.values())
    for seq in freq_dict:
        freq_dict[seq] = round(freq_dict[seq] / total_weight, 2)
    return freq_dict


def gen_read_frames(dna_seq):
    frames = []
    frames.append(translate_seq(dna_seq, 0))
    frames.append(translate_seq(dna_seq, 1))
    frames.append(translate_seq(dna_seq, 2))
    temp_seq = reverse_complement(dna_seq)
    frames.append(translate_seq(temp_seq, 0))
    frames.append(translate_seq(temp_seq, 1))
    frames.append(translate_seq(temp_seq, 2))
    return frames


def protein_from_rf(aa_seq) -> List[str]:
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            if aa == "M":
                current_prot.append("")
            for i, _ in enumerate(current_prot):
                current_prot[i] += aa
    return proteins


def all_proteins_from_orfs(seq, start_pos=0, end_pos=0, ordered=False):
    if end_pos > start_pos:
        rfs = gen_read_frames(seq[start_pos:end_pos])
    else:
        rfs = gen_read_frames(seq)

    res = []
    for rf in rfs:
        prots = protein_from_rf(rf)
        for p in prots:
            res.append(p)
    if ordered:
        return sorted(res, key=len, reverse=True)
