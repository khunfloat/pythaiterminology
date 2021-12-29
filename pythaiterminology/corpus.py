from typing import FrozenSet

from pythaiterminology.tools import get_corpus

_math_terminology = set()
_math_terminology_path = 'pythaiterminology/data/math_terminology.txt'

_physics_terminology = set()
_physics_terminology_path = 'pythaiterminology/data/physics_terminology.txt'

_chemical_terminology = set()
_chemical_terminology_path = 'pythaiterminology/data/chemical_terminology.txt'

_all_terminology = set()

def math_terminology() -> FrozenSet[str]:
    global _math_terminology
    if not _math_terminology:
        _math_terminology = get_corpus(_math_terminology_path)

    return frozenset(_math_terminology)

def physics_terminology() -> FrozenSet[str]:
    global _physics_terminology
    if not _physics_terminology:
        _physics_terminology = get_corpus(_physics_terminology_path)

    return frozenset(_physics_terminology)

def chemical_terminology() -> FrozenSet[str]:
    global _chemical_terminology
    if not _chemical_terminology:
        _chemical_terminology = get_corpus(_chemical_terminology_path)

    return frozenset(_math_terminology)

def all_terminology() -> FrozenSet[str]:
    global _all_terminology
    if not _all_terminology:
        _all_terminology = {*math_terminology(), 
                            *physics_terminology(), 
                            *chemical_terminology()}

    return frozenset(_all_terminology)