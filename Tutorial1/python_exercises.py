"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x % 2:
        return True
    else:
        return False


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    for i in range(0, len(word) // 2):
        if word[i] != word[-1-i]:
            return False
    return True


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    result = []
    for num in numlist:
        if is_odd(num):
            result.append(num)
    return result


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    result = {}
    for word in text.split(' '):
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(is_odd(5))
print(is_odd(12))
print(is_palindrome('12321'))
print(is_palindrome('1221'))
print(is_palindrome('12351'))
print(only_odds([1, 2, 3, 4, 5, 5, 9, 8]))
print(count_words("How much wood would a woodchuck chuck if a woodchuck could chuck wood?"))