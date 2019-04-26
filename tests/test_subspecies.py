# -*- coding: utf-8 -*-

import pytest
import botaxon


@pytest.mark.parametrize("test_input", ["Argyranthemum frutescens subsp. canariae"])
def test_single_subspecies(test_input):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, botaxon.SubSpeciesResult)
    assert botaxon.load(test_input).name == test_input


@pytest.mark.parametrize("test_input", ["Salix × ampherista subsp. yamatensis"])
def test_single_subspecies_with_hybrid_marker_on_species(test_input):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, botaxon.SubSpeciesResult)
    assert botaxon.load(test_input).name == test_input
