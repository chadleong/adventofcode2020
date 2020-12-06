import os

dir=os.path.dirname(os.path.realpath(__file__))

with open(dir+'\\inputs.txt', 'r', newline=None, encoding='utf-8') as f:
    l=[i.strip() for i in f]
    f.close()

def find_2020(arg):
    for i in range(len(arg)):
        first=int(arg[i])
        for j in range(i+1,len(arg)):
            if j<199:
                if first+int(arg[j+1])==2020:
                    print(first, int(arg[j+1]))
                    print(first*int(arg[j+1]))


find_2020(l)