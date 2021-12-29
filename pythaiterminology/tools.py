from typing import Union


def get_corpus(path: str, as_if: bool = False) -> Union[frozenset, list]:

    contents = []

    file = open(path, 'r', encoding='utf-8')
    contents = file.read().splitlines()
    file.close()

    if as_if:
        return contents

    contents = [line.strip() for line in contents]

    return frozenset(filter(None, contents))