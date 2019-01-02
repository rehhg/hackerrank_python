import os
from collections import Counter


def is_valid(s):
    return "YES" if contains_only_one_different_character_count(s) else "NO"


def contains_only_one_different_character_count(string):
    character_counts = Counter(string)
    if all_counts_are_equal(character_counts):
        return True
    else:
        for character in characterCounts:
            character_count_with_one_removed_character = character_counts.copy()
            character_count_with_one_removed_character[character] -= 1
            character_count_with_one_removed_character += Counter()  # remove zero and negative counts
            if allCountsAreEqual(character_count_with_one_removed_character):
                return True
    return False


def all_counts_are_equal(dict):
    return len(set(dict.values())) == 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = is_valid(s)

    fptr.write(result + '\n')

    fptr.close()
