from Bio import SeqIO
import sys

f = sys.argv[1]

record = SeqIO.read(f,'fasta')

print(record.seq)

