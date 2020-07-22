'''
tool.py method
fasta -> count_base()
file_name : str
count : dic

'''
import sys
class FASTA():
    def __init__(self,file_name):
        self.file_name = file_name
        self.count = {}
        self.length = 0
    def count_base(self):
        with open(self.file_name,'r') as handle:
            for line in handle:
                if line.startswith('>'):
                    continue
                line = line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
    '''
    def get_length(self):
        for k,v in self.count.items():
            self.length += v
    '''
    def __len__(self):
        for k,v in self.count.items():
            self.length += v
        return(self.length)

class FASTQ():
    def __init__(self,file_name):
        self.file_name = file_name
        self.read_num = 0
        self.seq = {}
    def count_read(self):
        cnt = 0
        with open(self.file_name,'r') as handle:
            for line in handle:
                if cnt%4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt%4 == 1:
                    seq = line.strip()
                    for i in seq:
                        if i in self.seq:
                            self.seq[i] += 1
                        else:
                            self.seq[i] = 1
                        
                elif cnt%4 == 3:
                    qual = line.strip()
                cnt += 1    
        
        


   
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'#usage: python {sys.argv[0]} [fasta]')
        sys.exit()
    file_name = sys.argv[1]
    #t = FASTA(file_name)
    #t.count_base()
    #t.get_length()
    a = FASTQ(file_name)
    a.count_read()
    print(a.seq)
    #print(t.count)
    #print(t.length)
    print(a.read_num)
'''
def setName(*arg):
    f_names = []
    fq_names = []
    vcf_names = []
    for i in arg:
        if i.find('.fasta'):
            f_names.append(str(i))
        elif i.find('.fastq')
            fq_names.append(str(i))
        elif i.find('.vcf'):
            vcf_names.append(str(i))
    for i in f_name:
        str(i[:-6]) = FASTA(i)
        str(i[:-6]).count_base()
    for i in fq_names:
        str(i[:-6]) = FASTQ(i)
        str(i[:-6]).count_read()
    for i in vcf_names:
        str(i[:-4]) = VCF(i)
        str(i[:-4]).vcf_read()
'''


















