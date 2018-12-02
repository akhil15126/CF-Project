import matplotlib.pyplot as plt
import numpy as np
import csv


filename="ml"
f=open(filename+".csv")
cs=csv.reader(f)
mainlist=list(cs)
mainlist.pop(0)


EPOCH=[]
NDCG=[]
HR=[]

for a in mainlist:
	EPOCH.append(int(a[0]))
	HR.append(float(a[1]))
	NDCG.append(float(a[2]))

plt.figure(0)
plt.title(filename.upper())
plt.plot(EPOCH[0::10],HR[0::10],linewidth=2.0)
plt.xlabel("EPOCHS")
plt.ylabel("HR@10")
plt.savefig(filename+"_HR.jpg")


plt.figure(1)
plt.title(filename.upper())
plt.plot(EPOCH[0::10],NDCG[0::10])
plt.xlabel("EPOCHS")
plt.ylabel("NDCG@10")
plt.savefig(filename+"_NDCG.jpg")


