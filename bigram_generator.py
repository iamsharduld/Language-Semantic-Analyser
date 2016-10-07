#from nltk import bigrams
from nltk import bigrams
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.corpus import gutenberg
import json

vals = {}

tri = []
c = 0
d = {}
for i in brown.categories():
	print i
	titi = bigrams(k.lower() for k in brown.words(categories = i))
	#c += len(titi)
	for j in titi:
		d[j] = d.get(j , 0) + 1
		c += 1
print len(d)
for i in reuters.categories():
	print i
	titi = bigrams(k.lower() for k in reuters.words(categories = i))
	#c += len(titi)
	for j in titi:
		d[j] = d.get(j , 0) + 1
		c += 1
print len(d)
for i in gutenberg.fileids():
	val = gutenberg.words(i)
	titi = bigrams(k.lower() for k in val)
	for j in titi:
		d[j] = d.get(j , 0) + 1
		c += 1


print len(d)
print c

from nltk.book import *
arr = []
for i in text1:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

print len(d)
print c

arr = []
for i in text1:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text2:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text3:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text4:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text5:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text6:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text7:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text8:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

arr = []
for i in text9:
	arr.append(i.lower())

titi = bigrams(arr)
#c += len(titi)
for j in titi:
	d[j] = d.get(j , 0) + 1
	c += 1

print c
print len(d)

from nltk.corpus import shakespeare as spp
jjj = 0
arr=[]
for i in spp.fileids():
	titi = spp.words(i)
	for j in titi:
		arr.append(j.lower())

	titi=bigrams(arr)

	for k in titi:
		d[k] = d.get(k , 0) + 1
		c+=1
		if(jjj<100):
			print k
			jjj+=1

print len(d)
print c



#for i in d:
	#print d[i] , i
fh = open('bigrams.json' , 'w+')
fh.read()
m = (d.keys())
m.sort()
for i in m:
	#print str(i[0])+" "+str(i[1])+ " "+str(i[2]) + " " + str(d[i]) + '\n'
	#fh.write(str(i[0])+" "+str(i[1])+ " "+str(i[2]) + " " + str(d[i]) + '\n')
	#print ' '.join((i[0], i[1], i[2])).encode('utf-8')
	#fh.write(' '.join((i[0], i[1], i[2] , str(d[i]))).encode('utf-8'))
	vals[' '.join((i[0], i[1])).encode('utf-8')] = str(d[i])
	#fh.write('\n')

json.dump(vals,fh)