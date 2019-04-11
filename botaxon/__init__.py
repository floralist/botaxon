from collections import deque, namedtuple

__VERSION__ = "0.1a0"


GenusResult = namedtuple("Genus", "name is_hybrid")

SpeciesResult = namedtuple("Species", "genus name is_hybrid")
SubSpeciesResult = namedtuple("SubSpecies", "species epithet")

VarietyResult = namedtuple("Variety", "species name")
SubVarietyResult = namedtuple("SubVariety", "species name")

FormResult = namedtuple("Form", "species name")
SubFormResult = namedtuple("SubForm", "species name")


VERBATIM_RANKS = {
    "subsp.": SubSpeciesResult,
    "var.": VarietyResult,
    "subvar.": SubVarietyResult,
    "f.": FormResult,
    "subf.": SubFormResult
}


class InvalidSpeciesError(Exception):
    pass


class InvalidSubTaxonError(Exception):
    pass


class InvalidVerbatimRankError(Exception):
    pass


def load(scientific_name, hybrid_marker="×"):

    if isinstance(scientific_name, str):
        scientific_name = scientific_name.split()

    scientific_name = deque(map(str, scientific_name))

    genus_name_or_hybrid_marker = scientific_name.popleft()
    if genus_name_or_hybrid_marker == "×":
        genus_is_hybrid = True
        genus_name = scientific_name.popleft()
    else:
        genus_is_hybrid = False
        genus_name = genus_name_or_hybrid_marker

    genus = GenusResult(genus_name, genus_is_hybrid)

    if not scientific_name:
        return genus

    species_name_or_hybrid_marker = scientific_name.popleft()
    if species_name_or_hybrid_marker == hybrid_marker:
        species_is_hybrid = True
        species_name = scientific_name.popleft()
    else:
        species_is_hybrid = False
        species_name = species_name_or_hybrid_marker

    species = SpeciesResult(genus, species_name, species_is_hybrid)

    if not scientific_name:
        return species

    verbatim_rank_or_species_name_leftover = scientific_name.popleft()
    if verbatim_rank_or_species_name_leftover in VERBATIM_RANKS.keys():
        infraspecific_rank = verbatim_rank_or_species_name_leftover

        if not scientific_name:
            raise InvalidSubTaxonError("species must be followed by an epithet")

        infraspecific_epithet = " ".join(scientific_name)
        subtaxon_cls = VERBATIM_RANKS.get(infraspecific_rank)

        if not subtaxon_cls:
            raise InvalidVerbatimRankError()

        return subtaxon_cls(species, infraspecific_epithet)

    species_name = "{} {}".format(species_name, " ".join(scientific_name))

    if hybrid_marker in species_name:
        raise InvalidSpeciesError()

    return SpeciesResult(genus, species_name, species_is_hybrid)
