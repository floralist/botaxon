import pytest
import botaxon


@pytest.mark.parametrize("test_input", ["Ocimum citriodorum", "Bartramia brachyphyllaviridissima"])
def test_single_species(test_input):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, botaxon.SpeciesResult)
    assert botaxon.load(test_input).name == test_input


@pytest.mark.parametrize("test_input", ["Ocimum × africanum"])
def test_single_species_with_hybrid_marker(test_input):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, botaxon.SpeciesResult)
    assert botaxon.load(test_input).name == test_input


@pytest.mark.parametrize("test_input", ["Ligularia sibirica lydiae"])
def test_composed_species(test_input):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, botaxon.SpeciesResult)
    assert botaxon.load(test_input).name == test_input


@pytest.mark.parametrize("test_input", ["Ocimum × africanum"])
def test_composed_species_with_hybrid_marker(test_input):
    parsed = botaxon.load(test_input)
    assert isinstance(parsed, botaxon.SpeciesResult)
    assert botaxon.load(test_input).name == test_input
