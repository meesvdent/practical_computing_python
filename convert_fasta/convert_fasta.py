# Convert fasta file to protein sequence


def read_codon_table(filename):
    table = {}
    with open(filename) as file:
        for line in file:
            split_line = line.split("\t")
            codon = split_line[0]
            amino_acid = split_line[1].split("\n")[0]
            table[codon.upper()] = amino_acid
    return table


def read_fasta(filename):
    complete_string = ""
    with open(filename) as file:
        counter = 0
        for line in file:
            if counter > 0:
                line = line.strip()
                complete_string += line
            counter += 1
    triplets = [complete_string[i:i+3] for i in range(0, len(complete_string), 3)]
    return triplets


def convert_to_amino_acid(triplets, codon_table):
    amino_acids = []
    for triplet in triplets:
        amino_acids.append(codon_table[triplet])
    return amino_acids


def main():
    codon_file = "./codonCodingTable.txt"
    codon_table = read_codon_table(codon_file)
    fasta_file = "./sequence.fasta"
    fasta_seq = read_fasta(fasta_file)
    print(convert_to_amino_acid(fasta_seq, codon_table))


if __name__ == "__main__":
    main()

