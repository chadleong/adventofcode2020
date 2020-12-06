import os

dir=os.path.dirname(os.path.realpath(__file__))

with open(dir+'\\inputs.txt', 'r', newline=None, encoding='utf-8') as f:
    l=[i.strip() for i in f]
    f.close()

#part 1
def find_2020_part1(arg):
    for i in range(len(arg)):
        first=int(arg[i])
        for j in range(i+1,len(arg)):
            if j<199:
                if first+int(arg[j+1])==2020:
                    print(first, int(arg[j+1]))
                    print(first*int(arg[j+1]))

#part 2
def find_2020_part2(arg):
    for i in range(len(arg)):
        first=int(arg[i])
        for j in range(len(arg)):
            if j<199:
                second=int(arg[j])
                for k in range(len(arg)):
                    if first+second+int(arg[k])==2020:
                        print(first, second, int(arg[k]))
                        print(first*second*int(arg[k]))

find_2020_part2(l)