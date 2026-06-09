text="ACGTTGCATGTCGCATGATGCATGAGAGCT"
k=4

counts ={}
for i in range(len(text)-k+1):
  kmer = text[i:i+k]
  counts[kmer]=counts.get(kmer,0)+1

max_count = max(counts.values())
print(" ".join(k for k,v in counts.items() if v ==max_count))
