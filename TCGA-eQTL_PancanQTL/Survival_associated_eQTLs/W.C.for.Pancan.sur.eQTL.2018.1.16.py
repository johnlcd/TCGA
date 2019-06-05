import re,os,sys
import urllib
import urllib2

def urlpin(X):
	urlc=[]
	for i in X:
		i=i.split(' ')
		for p in i:
			urlc.append(p)
	url=urlc[0]
	for i in range(1,len(urlc)):
		url=url+'+'+urlc[i]
	return url

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
urlqian='http://bioinfo.life.hust.edu.cn/PancanQTL/survival?page='

f1=open('/home/rongyu/datasave/TCGA-eQTL_PancanQTL/Survival_associated_eQTLs/Survival_associated_eQTLs.txt','w')
f1.write('cancer.type')
f1.write('\t')
f1.write('SNP.ID')
f1.write('\t')
f1.write('SNP.position.hg19')
f1.write('\t')
f1.write('Alleles(A/a)')
f1.write('\t')
f1.write('log-rank.pval')
f1.write('\t')
f1.write('sample.size')
f1.write('\t')
f1.write('Median.survival.time.AA')
f1.write('\t')
f1.write('Median.survival.time.Aa')
f1.write('\t')
f1.write('Median.survival.time.aa')
f1.write('\n')



for i in range(1,1482):
	url=urlqian+str(i)
	try:
		print(url)
		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		
		page=response.read()
		p1='<td class="text-center">.*?</td>'
		pattern1 = re.compile(p1)
		matcher1 = re.findall(pattern1,page)
		if matcher1:
			temp=matcher1
			num=1
			for p in temp:
				p=p.replace('<td class="text-center">','')
				p=p.replace('</td>','')
				if num != 9:
					f1.write(p)
					f1.write('\t')
					num+=1
				else:
					f1.write(p)
					f1.write('\n')
					num=1			
	except urllib2.URLError, e:
		f1.write(str(i))
		if hasattr(e,"code"):
			f1.write('nan')
			print e.code
		if hasattr(e,"reason"):
			print e.reason
			f1.write('nan')
		f1.write('\n')
f1.close
