hash = "b8e46064c5cb98321ab378f546d2641881b43563"

words = ["walle", "wall-e", "logitech", "tuerca"]


def all_casings(input_string):
    if not input_string:
        yield ""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing


if __name__ == "__main__":
    print("Cuarto reto\n")

    """
    for w_initial in words:
        print("Trying all permutations of: " + w_initial)
        w_permut = list(all_casings(w_initial))

        for word in w_permut:
            result = hashlib.sha1(word.encode())
            hashres = result.hexdigest()
            if hashres == hash:
                print("FOUND!!!!!")
    """
