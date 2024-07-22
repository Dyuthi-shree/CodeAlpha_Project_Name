import random

Nucleotides = ["A", "C", "G", "T"]

# Check the sequence to make sure it is a DNA String.
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

# Count the frequency of nucleotides in the sequence.
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

# Generate a random DNA sequence of a given length.
def generateRandomDNA(length=50):
    return ''.join(random.choices(Nucleotides, k=length))
