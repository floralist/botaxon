botaxon
=======

botaxon is a taxonomic parser for (sub)species botanical names.

It has been used against 3 million names. Not released yet, the tests are coming !


Usage
-----

```python
>>> import botaxon

>>> botaxon.load("Plumeria")
Genus(name='Plumeria', is_hybrid=False)

>>> botaxon.load("Ocimum × citriodorum")
Species(genus=Genus(name='Ocimum', is_hybrid=False), name='citriodorum', is_hybrid=True)

>>> botaxon.load("Cannabis sativa var. indica")
Variety(species=Species(genus=Genus(name='Cannabis', is_hybrid=False), name='sativa', is_hybrid=False), name='indica')
```