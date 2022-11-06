ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = ALPHABET_LOWER.upper()
NUMBERS = "0123456789"
SYMBOLS=",;:!?%*§ù*$^=+&()[]@_-€\"\' "


def caesar_cipher(word: str, key: int) -> str:
    new_word = []
    for pos in range(len(word)):
        letter = word[pos]
        if letter in SYMBOLS:
            new_word += [
                SYMBOLS[
                    (SYMBOLS.index(letter)) # Symbols are not affected
                ]
            ]
        elif letter in ALPHABET_LOWER:
            new_word += [
                ALPHABET_LOWER[
                    (ALPHABET_LOWER.index(letter) + key) % len(ALPHABET_LOWER)
                ]
            ]
        elif word[pos] in ALPHABET_UPPER:
            new_word += [
                ALPHABET_UPPER[
                    (ALPHABET_UPPER.index(letter) + key) % len(ALPHABET_UPPER)
                ]
            ]
        elif word[pos] in NUMBERS:
            new_word += [NUMBERS[(NUMBERS.index(letter) + key) % len(NUMBERS)]]

    return "".join(new_word)


def caesar_decipher(word: str, key: int) -> str:
    return caesar_cipher(word, -key)


def bf_caesar(cipher_text: str) -> list:
    """
    Takes a Caesar cipher text and return all the possibilities
    for the decipher text as a list.
    """
    possibilities = []
    for i in range(len(ALPHABET_LOWER)):
        possibilities.append(caesar_cipher(cipher_text, i))
    return possibilities


def nb_match(string: str, path: str) -> int:
    """
    Takes a string in first argument and a path to a file in second argument.
    The file is a dictionary which contains one word per line.
    This function check if any word contained in the file is
    present in the first argument and return the number of words matching.
    """
    with open(path, "r") as f:
        dictionary = f.read().splitlines()
    matches = sum([dictionary.count(word) for word in string.split()])
    return matches or -1


def bf_common_caesar(cipher_text: str, path: str) -> str:
    """
    Takes a Caesar cipher text in first argument and a filepath in second argument.
    This function return the decoded string which has the most match of the word
    in the file.
    """
    possibilities = bf_caesar(cipher_text)
    matches_list = list(map(lambda p: nb_match(p, path), bf_caesar(cipher_text)))
    return possibilities[matches_list.index(max(matches_list))]


assert caesar_cipher("Caesar", 3) == "Fdhvdu"
assert caesar_decipher("Fdhvdu", 3) == "Caesar"
assert caesar_cipher("Hello Z19", 7) == "Olssv G86"
assert caesar_decipher("Olssv G86", 7) == "Hello Z19"
