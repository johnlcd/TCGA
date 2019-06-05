import re,os,sys

os.system('cut -f1 Survival_associated_eQTLs.txt > temp')
os.system('sort temp > 1')
os.system('uniq 1 > temp')
f1=open('temp','r')
m1=f1.readlines()
cancer=[]
for p1 in m1:
	p1=p1.strip().split('\t')
	cancer.append(p1[0])
f1.close()

os.system('mkdir /home/rongyu/datasave/TCGA-eQTL_PancanQTL/Survival_associated_eQTLs/split')

for c in cancer:
	f1=open('/home/rongyu/datasave/TCGA-eQTL_PancanQTL/Survival_associated_eQTLs/Survival_associated_eQTLs.txt','r')
	m1=f1.readlines()
	f2=open('/home/rongyu/datasave/TCGA-eQTL_PancanQTL/Survival_associated_eQTLs/split/%s.Survival_associated_eQTLs.txt'%c,'w')
	bar=m1[0].strip().split('\t')
	for p in bar:
		f2.write(p)
		f2.write('\t')
	f2.write('\n')
	for i in range(1,len(m1)):
		p1=m1[i].strip().split('\t')
		if c == p1[0]:
			for p in p1:
				f2.write(p)
				f2.write('\t')
			f2.write('\n')
	f1.close()
	f2.close()