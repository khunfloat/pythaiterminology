from pythaiterminology.corpus import math_terminology, physics_terminology, chemical_terminology, all_terminology

def test_math_terminology():
    assert type(math_terminology()) == type(frozenset())

def test_physics_terminology():
    assert type(physics_terminology()) == type(frozenset())

def test_chemical_terminology():
    assert type(chemical_terminology()) == type(frozenset())

def test_all_terminology():
    assert type(all_terminology()) == type(frozenset())