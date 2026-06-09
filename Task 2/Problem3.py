dna = input().strip()

complement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

reverse_complement = ""

for nucleotide in reversed(dna):
    reverse_complement += complement[nucleotide]

print(reverse_complement)
