import matplotlib.pyplot as plt
import numpy as np

filename="Kolodziejczyk"

f=open(filename)
EPOCH=[]
HR=[]
NDCG=[]
AUC=[]
lines=f.readlines()
for l in lines:
	if("best" in l):
		continue
	if("Epoch" in l):
		ep=l.split("Epoch ")[1]
		ep=ep.split(" ")[0]
		EPOCH.append(int(ep))

		hr=l.split("HR = ")[1]
		hr=hr.split(",")[0]
		HR.append(float(hr))

		nd=l.split("NDCG = ")[1]
		nd=nd.split(" ")[0]
		NDCG.append(float(nd))

		nd=l.split("AUC = ")[1]
		nd=nd.split(" ")[0]
		AUC.append(float(nd))

plt.figure(0)
plt.title(filename.upper())
plt.plot(EPOCH[0::5],HR[0::5],linewidth=2.0)
plt.xlabel("EPOCHS")
plt.ylabel("HR@10")
plt.savefig(filename+"_HR.jpg")


plt.figure(1)
plt.title(filename.upper())
plt.plot(EPOCH[0::5],NDCG[0::5])
plt.xlabel("EPOCHS")
plt.ylabel("NDCG@10")
plt.savefig(filename+"_NDCG.jpg")

import csv
# f=open(filename+".txt")
cf=csv.writer(open(filename+'.csv', 'a'))
data=[tuple(EPOCH),tuple(HR),tuple(NDCG),tuple(AUC)]
data=list(zip(*data))
cf.writerow(('EPOCHS','HR','NDCG','AUC'))
for a in data:
	cf.writerow(a)

