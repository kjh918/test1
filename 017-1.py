import sys
import gzip

if len(sys.argv) != 2:
    print(f'usage: python {sys.argv[0]} [fasta]')
    sys.exit()

f = sys.argv[1]
d = {}

with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode('utf-8')
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

print(d)
total = 0 
for k,v in d.items():
    total += v
print(total)
print(d)
'''
p = open('write_sample.txt','w')
for k, v in d.items():
    p.write(str(k)+':'+str(v)+'\n')
p.close()
'''
with open('result_1.txt','w') as handle:
    handle.write(f"A: {d['A']}\n")    
    handle.write(f"C: {d['C']}\n")    
    handle.write(f"G: {d['G']}\n")    
    handle.write(f"T: {d['T']}\n")    

             
                          
