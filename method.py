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
    
    def get_length(self):
        for k,v in self.count.items():
            self.length += v
    
    #def __len__(self):
        #for k,v in self.count.items():
            #self.length += v
        #return(self.length)

class FASTQ():
    def __init__(self,file_name):
        self.file_name = file_name
        self.read_num = 0

    def count_read(self):
        cnt = 0
        with open(self.file_name,'r') as handle:
            for line in handle:
                if cnt%4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt%4 == 1:
                    seq = line.strip()
                elif cnt%4 == 3:
                    qual = line.strip()
                cnt += 1

import pandas as pd 
class VCF():
    def __init__(self,file_name):
        self.file_name = file_name
        self.vcf_line = []
        self.vcf_df = pd.DataFrame()
        self.var_count = {}
    def make_var(self):
        with open(self.file_name,'r') as handle:
            for line in handle:
                line = line.replace('\n','')
                if line.startswith('##'):
                    continue
                elif line.startswith('#'):
                    line = line.replace('#','')
                    col = line.split('\t')
                    continue
                line = line.split('\t')
                d = dict(zip(col,line))
                self.vcf_line.append(d)
            self.vcf_df = pd.DataFrame(self.vcf_line)
            return self.vcf_df
    def variable_count(self):
        self.var_count = {'SNP':0,'INS':0,'DEL':0}
        for i in self.vcf_line:
            if len(i['REF']) == len(i['ALT']):
                self.var_count['SNP'] += 1
            elif len(i['REF']) < len(i['ALT']):
                self.var_count['INS'] += 1
            elif len(i['REF']) > len(i['ALT']):
                self.var_count['DEL'] += 1
        return self.var_count

'''
        for i in range(len(df.index)):
            if self.vcf_df['REF'][i] == self.vcf.df['ALT'][i]:
                
        self.vcf_df['REF'])
            if len(i['REF']) == len(i['ALT']):
                self.var_count['SNP'] = 1
            elif len(i['REF']) < len(i['ALT']):
                self.var_count['INS'] += 1
            elif len(i['REF']) > len(i['ALT']):
                self.var_count['DEL'] += 1
        return self.var_count
'''    
        
def setName(*arg):
    f_names = []
    fq_names = []
    vcf_names = []
    for h in arg:
        for i in h:
            if i.endswith('.fasta'):
                f_names.append(str(i))
            elif i.endswith('.fastq'):
                fq_names.append(str(i))
            elif i.endswith('.vcf'):
                vcf_names.append(str(i))
    for i in range(len(f_names)):
        globals()['fasta_{}'.format(i)] = FASTA(f_names[i])
        globals()['fasta_{}'.format(i)].count_base()
        globals()['fasta_{}'.format(i)].get_length()
        print(globals()['fasta_{}'.format(i)].count)
        print(globals()['fasta_{}'.format(i)].length)
        print('\n')
    for i in range(len(fq_names)):
        globals()['fastq_{}'.format(i)] = FASTQ(fq_names[i])
        globals()['fastq_{}'.format(i)].count_read()
        print(globals()['fastq_{}'.format(i)].read_num)
        print('\n')
    for i in range(len(vcf_names)):
        globals()['vcf_{}'.format(i)] = VCF(vcf_names[i])
        print(globals()['vcf_{}'.format(i)].make_var())
        globals()['vcf_{}'.format(i)].variable_count()
        print(globals()['vcf_{}'.format(i)].var_count)

if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print(f'#usage: python {sys.argv[0]} [fasta]')
#        sys.exit()
     print(sys.argv[1:])
     setName(sys.argv[1:])

'''        
def setName(*arg):
    f_names = []
    fq_names = []
    vcf_names = []
    for h in arg:
        for i in h:
            if i.find('.fasta'):
                f_names.append(str(i))
            elif i.find('.fastq'):
                fq_names.append(str(i))
            elif i.find('.vcf'):
                vcf_names.append(str(i))
    for i in range(len(f_names)):
        print(f_names[i])
        print('\n')
    for i in range(len(fq_names)):
        print(fq_names[i])
        print('\n')
    for i in range(len(vcf_names)):
        print(vcf_names[i])

if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print(f'#usage: python {sys.argv[0]} [fasta]')
#        sys.exit()
     print(sys.argv[1:])
     setName(sys.argv[1:])
'''


















