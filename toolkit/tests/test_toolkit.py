#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import random

import pytest

from toolkit.main import NUCLEOTIDES, nucleotide_frequency, transcript, validate_seq


@pytest.fixture
def input_data():
    return "".join(random.choices(NUCLEOTIDES, k=random.randrange(1, 20)))


def test_validate_seq_happy_path(input_data):
    validated = validate_seq(input_data)
    assert validated == input_data


def test_validate_seq_sad_path():
    input_data = "".join(random.choices(["b", "x", "g", "f"], k=20))
    validated = validate_seq(input_data)
    assert not validated


def test_count_nucleotide_frequency(input_data):
    frequency = nucleotide_frequency(input_data)
    assert frequency == {
        nuc: input_data.count(nuc) for nuc in set(input_data)
    }


def test_count_nucleotide_frequency_sad_path():
    frequency = nucleotide_frequency(validate_seq("asdioawhdposaf"))
    assert not frequency


def test_transcipt(input_data):
    transcripted = transcript(validate_seq(input_data))
    assert (
        nucleotide_frequency(transcripted)["U"]
        == nucleotide_frequency(input_data)["T"]
    )
