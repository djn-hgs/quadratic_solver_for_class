import math

def count_shuffles(word: str) -> int:
    unique_chars = set(word)
    histogram = {a: word.count(a) for a in unique_chars}
    divisor = math.prod(math.factorial(n) for n in histogram.values())
    dividend = math.factorial(len(word))

    return dividend // divisor

def get_shuffles(word: str) -> [str]:
    pass

