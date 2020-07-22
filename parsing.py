import sys
f = sys.argv[1]

x = ''
with open(f,'r') as f:
    for i in f.read():
        if i.startswith('>'):
            continue
        x += i.replace('\n','')
print('')        
print(x) 
