from DNAToolkit import validateSeq, countNucFrequency, generateRandomDNA

# Main function to automate the process.
def main():
    # Option to use a random DNA sequence or user input.
    use_random = input("Use a random DNA sequence? (yes/no): ").strip().lower()
    if use_random == 'yes':
        dna_seq = generateRandomDNA()
        print(f"Generated random DNA sequence: {dna_seq}")
    else:
        dna_seq = input("Enter a DNA sequence: ").strip().upper()
        
    # Validate the DNA sequence.
    valid_seq = validateSeq(dna_seq)
    if not valid_seq:
        print("Invalid DNA sequence!")
        return

    # Print the validated DNA sequence and nucleotide frequency.
    print("Validated DNA Sequence:", valid_seq)
    print("Nucleotide Frequency:", countNucFrequency(valid_seq))

if __name__ == "__main__":
    main()
