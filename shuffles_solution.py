import math

count_shuffles = lambda word: math.factorial(len(word)) // math.prod(map(math.factorial, map(word.count, set(word))))


def get_shuffles(word: str) -> [str]:
    pass

