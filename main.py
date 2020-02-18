import sys
import numpy as np

maxSlices = 0;
number_of_types = 0;
Ntypes = [];

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
    writeFile(Ntypes,pizzadick)

def writeFile(Ntypes,pizzadick):
    line = []
    typeCount = 0
    for t in Ntypes:
        if t in pizzadick and pizzadick[t]>0:
            typeCount += 1
        line += str(pizzadick[t]) + ' '
    outputArray(line, pizzadick)
    print(line, typeCount, pizzadick)

def outputArray(line, pizzadick):
    newArr = []
    for i in line:
        if i == 1:
            newArr.append(pizzadick[i])
    print(newArr)



     # write typeCount
     # write line

# def rightplace(Ntypes,pizzadick):
#     pizzadick
#     with open("output.txt", 'w') as f:

#         f.write('{}\n'.format(len(cutter.slices)))
#         for slic in cutter.slices:
#             f.write(' '.join([str(item) for item in slic]) + '\n')




# print(str(count))
# print(pizzadick)








# read_file('data/a_example.in')


# class Pizza:
#     def init(self, pizzaType, number_of_slices):
#         self.pizzaType = pizzaType
#         self.number_of_slices = number_of_slices


def main():
#   pizza = Pizza(0, 3)
#   pass

    read_file('data/a_example.in')

if (name == 'main'):
  main()
