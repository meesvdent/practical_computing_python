# Exercises of session on 17-11-2021


def create_lists():
    list_1 = list(range(1, 10, 2))
    print(list_1)
    list_2 = list(range(1, 10))
    del(list_2[2:5])
    print(list_2)
    list_3 = list(range(10, 0, -1))
    print(list_3)
    list_4_1 = list(range(1, 6))
    list_4_2 = list(range(4, 0, -1))
    list_4 = list_4_1 + list_4_2
    print(list_4)

def sequence_complement(sequence):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    complementary_seq = [complement[x] for x in sequence]
    return complementary_seq

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    create_lists()

    # Test complementary sequence generation
    seq = "ACTGCTTACGCTTA"
    complementary = sequence_complement(seq)
    complementary = "".join(complementary)
    print(complementary)

    # Test fibonacci
    fibo_9 = fibonacci(9)
    print(fibo_9)


if __name__ == "__main__":
    main()

