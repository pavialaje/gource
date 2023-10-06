def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    len_th = 0
    for i in dna:
        len_th=len_th+1

    return len_th


get_length('ATCGAT')
get_length('ATCG')


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    dna1 = get_length(dna1)
    dna2 = get_length(dna2)
    return True if dna1 > dna2 else False


is_longer("ATCG","AT")
is_longer("ATCG","ATCGGA")


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


count_nucleotides('ATCGGC', 'G')
count_nucleotides('ATCTA', 'G')


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return True if dna2 in dna1 else False


contains_sequence('ATCGGC', 'GT')
contains_sequence('ATCGGC', 'GG')


def is_valid_sequence(sequence):
    """ (str)-> bool
    Return True if input DNA sequence is valid one else return false.
    If all Letters in sequence contains only 'A', 'T', 'C', 'G' are valid.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('atGGC')
    False
    """
    dna_nucl = 'A', 'T', 'C', 'G'
    resp = True
    for char in sequence:
        if char in dna_nucl:
            resp = True
        else:
            resp = False
            break

    return resp


is_valid_sequence('ATCGGC')
is_valid_sequence('Aadf')


def insert_sequence(seq1, seq2, ind):
    """
    (str, str, int) -> str
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGGGCGC', 'AT', 6)
    'CCGGGCATGC'
    """
    if is_valid_sequence(seq1) and is_valid_sequence(seq2):

        return seq1[:ind] + seq2 + seq1[ind:]


insert_sequence("CCgGG", 'AT', 2)
insert_sequence('CCGGGCGC', 'AT', 6)

def get_complement(nuc):
    """
    (str)->str

    This function will return the complementary base parirs of given nucleotide
    >>> get_complement('A')
    T
    >>> get_complement('C')
    G
    """
    if is_valid_sequence(nuc):
        if nuc == 'A':
            return 'T'
        elif nuc == 'T':
            return 'A'
        elif nuc == 'C':
            return 'G'
        elif nuc == 'G':
            return 'C'

get_complement('C')

def get_complementary_sequence(seq):
    '''
    (str)-> str
    returns the complementary sequence of input nucleotide string
    >>get_complementary_sequence('ACGTTA')
    TGCAAT
    '''
    if is_valid_sequence(seq):
        seq_val = ''
        for let in seq:
            seq_val  =seq_val+get_complement(let)
        return seq_val
get_complementary_sequence('ACGTTA')