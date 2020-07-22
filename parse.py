import sys 
import json
'''
def readtxt(file_name: str) -> str:
    ret = ''
    with open(file_name,'r') as handle:
        for i in handle:
            if i.startswith('>'):
                continue
            ret += i
    return ret


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('#suage: python {sys.argv[0]} [txt]')
        sys.exit()
    file_name = sys.argv[1]
    txt = readcsv(file_name)
    print(txt)
'''


def readcsv(file_name: str) -> str:
    d ={}
    cont_list = []
    with open(file_name,'r') as handle:
        for i in handle:
            if i.startswith('#'):
                a = i.replace('#','')
                col = a.split(',')
            else:
                cont = i.split(',')
                cont_list.append(cont)
        return cont_list


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('#suage: python {sys.argv[0]} [txt]')
        sys.exit()
    file_name = sys.argv[1]
    txt = readcsv(file_name)
    print(txt)

'''
def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith('#'):
                header = line.strip().split("\t")
                continue
            splitted = line.split().split('\t')
            d = dict(zip(header,splitted))
            ret.append(d)

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith('#'):
                header = line.strip().split(",")
                continue
            splitted = line.split().split(',')
            d = dict(zip(header,splitted))
            ret.append(d)
    return ret

def to_json(l: list) -> None:
    with open('read_sample.json','w') as handle:
        json.dump(l,handle,indent=4)

'''
