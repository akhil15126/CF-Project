import numpy as np

f=open("newu.data")

f_train=open("training", "w")
f_test=open("testing","w")
f_neg=open("negatives","w")

nusers=943
nitems=1682

lines=f.readlines()
prev_user=1
items=[]
prevl=None
T=[]
totalitems=np.arange(nitems)+1
for e,l in enumerate(lines):

	l=l.split("\t")
	user=int(l[0])
	if(user==prev_user):
		items.append(int(l[1]))
		if(e!=0):
			f_train.write("\t".join(prevl))

	else:
		s=list(set(totalitems)-set(items))
		neg=[]
		neg=s[:900]
		neg=[str(a) for a in neg]
		f_neg.write("("+str(prevl[0])+","+str(prevl[1])+")\t")
		f_neg.write("\t".join(neg))
		f_neg.write("\n")
		f_test.write("\t".join(prevl))
		items=[]

		prev_user=user
	prevl=l

s=list(set(totalitems)-set(items))
neg=[]
neg=s[:900]
neg=[str(a) for a in neg]
f_neg.write("("+str(prevl[0])+","+str(prevl[1])+")\t")
f_neg.write("\t".join(neg))
f_neg.write("\n")
f_test.write("\t".join(prevl))

f.close()
f_test.close()
f_train.close()
f_neg.close()
# print(min(T))