def hash_func(chars):
    """This function hashes an input string"""

    hashed = 7
    possible_chars = "acdegilmnoprstuw"
    for i in range(len(chars)):
        hashed = hashed * 37 + possible_chars.index(chars[i])
    return hashed


def reverse_hash(hashed):
    """This function finds the input string that produced the hash, which is
    defined in the hash_func(chars) function.
        >>> reverse_hash(680131659347)
        'leepadg'
    """

    possible_chars = "acdegilmnoprstuw"
    input_chars = []
    i = 0

    # Hashed is initiated at 7, so it will be at least that.
    while hashed > 7:
        # if hashed is divisible by 37, the letter must be at index 0
        if hashed % 37 == 0:
            input_chars.append(possible_chars[i])
            # reset index to 0 and divide by 37 to continue
            i = 0
            hashed /= 37
        else:
            # subtract 1 from the hash and add 1 to the index to check next.
            hashed -= 1
            i += 1
    # reverse list for correct orer (since we found last letter first)
    # join the list.  a stack would work well for this problem as well.
    input_chars.reverse()
    return "".join(input_chars)


print reverse_hash(930846109532517)


#####################################################################
# END OF CHALLENGE: code below to run doctests.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
