import sys

def read_file(filename):
    with open(filename, 'r') as f:
        maxSlices, Ntypes = f.readline().split()
        number_of_types = f.readline()
        # print(maxSlices)
        Ntypes = [int(t.rstrip() ) for t in number_of_types.split(' ')]
        # print(Ntypes)
        checkMaxslice(maxSlices, number_of_types, Ntypes)

def checkMaxslice(maxSlices, number_of_types, Ntypes):
    count = 0
    Ntypes.sort(reverse = True)
    pizzadick = {}
    for i in Ntypes:
        countS = 0
        if count <= int(maxSlices) - i:
            count = count + i
            countS+=1
        pizzadick[i]=countS
    write_file(output(Ntypes,pizzadick), count)

def write_file(output, count):
    # print(output)
    # print(count)
    with open("output.txt", 'w') as f:
        f.write('{}\n'.format(count))
        f.write(' '.join([str(item) for item in output]) + '\n')

def output(Ntypes, pizzadick):
    orderTypes = []
    Ntypes.sort()
    for i in range(len(Ntypes)):
        if Ntypes[i] in pizzadick and pizzadick[Ntypes[i]] > 0:
            orderTypes.append(i)
    return orderTypes

def main():
#   pizza = Pizza(0, 3)
#   pass
    read_file('data/e_also_big.in')

if (__name__ == '__main__'):
    main()
