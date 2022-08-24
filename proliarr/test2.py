#Three lines to make our compiler able to draw:
import sys
import matplotlib
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
workbook = pd.read_excel('python.xlsx')
# Print the 1st value of the Product column
stime = []
etime= []
state = []
ID = []
data = []
tuple1 =[]
for i in range(0,63):
    datetime1 = (workbook['Start time'].iloc[i])
    datetime2 = (workbook['End time'].iloc[i])

    st = (workbook['State'].iloc[i])
    id = (workbook['MachineID'].iloc[i])
    stime.append(datetime1)
    etime.append(datetime2)
    ID.append(id)
    state.append(st)

astopedlist=[]
bstopedlist=[]
cstopedlist=[]
aworklist=[]
bworklist=[]
cworklist=[]
cideallist=[]
bideallist=[]
aideallist=[]
for i in range (0,63):
    x=(stime[i],etime[i],ID[i],state[i])
    data.append(x)
    if 'A' in x and 'Stopped' in x:
        astopedlist.append(x)
    elif 'B' in x and 'Stopped' in x:
        bstopedlist.append(x)
    elif 'C' in x and 'Stopped' in x:
        cstopedlist.append(x)
    elif 'C' in x and 'Working' in x:
        cworklist.append(x)
    elif 'A' in x and 'Working' in x:
        aworklist.append(x)
    elif 'B' in x and 'Working' in x:
        bworklist.append(x)
    elif 'B' in x and 'Idle' in x:
        bideallist.append(x)
    elif 'C' in x and 'Idle' in x:
        cideallist.append(x)
    elif 'A' in x and 'Idle' in x:
        aideallist.append(x)


for i in astopedlist:
    print(type(i[0]))
    x=np.array([i[0], i[1]])
    print(x)
    y=np.array(["A","A"])
    plt.plot(x, y,color='red')

for i in aworklist:
    x = np.array([i[0], i[1]])
    print(x)
    y = np.array(["A", "A"])
    plt.plot(x, y,color='blue')

for i in aideallist:
    x = np.array([i[0], i[1]])
    print(x)
    y = np.array(["A", "A"])
    plt.plot(x, y,color='green')

for i in bstopedlist:
    print(type(i[0]))
    x=np.array([i[0], i[1]])
    print(x)
    y=np.array(["B","B"])
    plt.plot(x, y,color='red')

for i in bworklist:
    x = np.array([i[0], i[1]])
    print(x)
    y = np.array(["B", "B"])
    plt.plot(x, y,color='blue')

for i in bideallist:
    x = np.array([i[0], i[1]])
    print(x)
    y = np.array(["B", "B"])
    plt.plot(x, y,color='green')

for i in cstopedlist:
    print(type(i[0]))
    x=np.array([i[0], i[1]])
    print(x)
    y=np.array(["C","C"])
    plt.plot(x, y,color='red')

for i in cworklist:
    x = np.array([i[0], i[1]])
    print(x)
    y = np.array(["C", "C"])
    plt.plot(x, y,color='blue')

for i in cideallist:
    x = np.array([i[0], i[1]])
    print(x)
    y = np.array(["C", "C"])
    plt.plot(x, y,color='green')
plt.title('Machine status')
plt.ylabel('Machine ID ', fontsize=18)
plt.xlabel('status per hour', fontsize=16)



plt.show()

# print(astopedlist)
# print(len(astopedlist))
# print(bstopedlist)
# print(cstopedlist)
# print(aworklist)
# print(bworklist)
# print(cworklist)