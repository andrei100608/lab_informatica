import sys
sys.path.append('usr/local/lib/python3.7/syte-packages')
import time
from random import randint
import matplotlib.pyplot as plt

dimensione = [100,1000,10000,100000,1000000,10000000]
tempi_l = []
tempi_ins=[]

for elem in dimensione:
    l = [f"ogg{i}" for i in range(1,elem+1)]
    ins = {f"ogg{i}" for i in range(1,elem+1)}

    count1 = 0
    start1 = time.perf_counter()
    while (count1<10):
        num = randint(1,elem+1)
        stringa = "ogg"+str(num)
        if (stringa in l):
            pass
        count1 +=1
    end1 = time.perf_counter()
    diff1 = (end1-start1)
    tempi_l.append(diff1)

    count2 = 0
    start2 = time.perf_counter()
    while (count2<10):
        num = randint(1,elem+1)
        stringa = "ogg"+str(num)
        if (stringa in ins):
            pass
        count2 +=1
    end2 = time.perf_counter()
    diff2 = (end2-start2)
    tempi_ins.append(diff2)

#print(dimensione)
#print(tempi_l)
#print(tempi_ins)

plt.plot(dimensione,tempi_l)

plt.xlabel("Dimensione")
plt.ylabel("Tempo")

plt.show()


plt.plot(dimensione,tempi_ins)

plt.xlabel("Dimensione")
plt.ylabel("Tempo")

plt.show()