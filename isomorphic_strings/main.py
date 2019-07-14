
def is_isomorphic(word : str, other: str) -> bool:
    """
    Determines whether two strings that are given in the argument, are isomorphic or not.
    """
    chars = {}
    for i in range(len(word)):
        try:
            if word[i] in chars and chars[word[i]] != other[i]:
                return False
            else:
                chars[word[i]] = other[i]
        except IndexError:
                return False
    return True


if __name__ == "__main__":
    print(is_isomorphic("gecik", "qwer"))