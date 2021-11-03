from typing import TypeVar, Generic, List, Sequence

# run via mypy (optional static type checker for python)
# pip install mypy
# Command: mypy basics/typing_and_generics/generics.py

# or run vec_sum_hardcode_edition and vec_sub_hardcode_edition

T = TypeVar('T', List[int], List[float])


def vec_sum(vec1: T, vec2: T) -> T:  # we can only hint about the correct type in python
    if len(vec1) == len(vec2):
        return [a + b for a, b in zip(vec1, vec2)]
    else:
        raise Exception('vectors have a different length')


def vec_sub(vec1: T, vec2: T) -> T:
    if len(vec1) == len(vec2):
        return [a - b for a, b in zip(vec1, vec2)]
    else:
        raise Exception('vectors have a different length')


# hard code decorator
def hard_code(func):
    def wrapper(vec1, vec2):
        if isinstance(vec1, list) and isinstance(vec2, list) and all(isinstance(item, int) for item in vec1) and all(
                isinstance(item, int) for item in vec2):
            if len(vec1) == len(vec2):
                return func(vec1, vec2)
            else:
                raise Exception('vectors have a different length')
        else:
            raise Exception('wrong type')
    return wrapper


@hard_code
def vec_sum_hardcode_edition(vec1: T, vec2: T) -> T:
    return [a + b for a, b in zip(vec1, vec2)]


@hard_code
def vec_sub_hardcode_edition(vec1: T, vec2: T) -> T:
    return [a - b for a, b in zip(vec1, vec2)]


if __name__ == "__main__":
    print(vec_sub([1, 2], [3, 4]))
    print(vec_sum([1, 2], [3, 4]))
    print(vec_sub_hardcode_edition([1, 2], [3, 4]))
    print(vec_sum_hardcode_edition([1, 2], [3, 4]))
