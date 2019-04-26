# -*- coding: utf-8 -*-

import pytest
import botaxon


@pytest.mark.parametrize("test_input, expected_class", [("Ocimum", botaxon.GenusResult)])
def test_genus(test_input, expected_class):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, expected_class)
    assert parsed.is_hybrid is False
    assert parsed.name == test_input


@pytest.mark.parametrize("test_input, expected_class", [("× Astroworthia", botaxon.GenusResult)])
def test_hybrid_genus(test_input, expected_class):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, expected_class)
    assert parsed.is_hybrid is True
    assert parsed.name == test_input
