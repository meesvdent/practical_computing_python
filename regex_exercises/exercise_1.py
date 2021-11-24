import regex as re


def match_int(string):
    return re.findall("[0-9]", string)


def find_arginine(sequence):
    return re.findall("CG[A|T|C|G]|AG[A|G]", sequence)


def find_usage(string):
    return re.findall(r"use\b|usage", string)


def find_triple_repeats(string):
    return re.findall(r"A{3}|T{3}|C{3}|G{3}", string)


def find_tata(string):
    return re.findall(r"TAT.AT|TATA.T", string)


def main():
    test_string = "This is a test string with 4 numbers, the first 1 we just had, the 3rd and 4th are here."
    test_sequence = "ATGGCCTTTGCACCTATGGGGCCCGAGGCCTCGTTCTTCGACGTTTTGGACCGACACAGGGAGTCCCTGCTGGCTGCCCTGAGGAGAGGTGGCAGGG"
    print(match_int(test_string))
    print(find_arginine(test_sequence))
    use_string = "use, used, usage, use, used, usage"
    print(find_usage(use_string))
    print(find_triple_repeats(test_sequence))
    tata_string = "TATAAT TATCAT TATACT TATCCT TATAAT"
    print(find_tata(tata_string))


if __name__ == "__main__":
    main()

