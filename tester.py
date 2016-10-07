import json
from nltk import trigrams
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import wordpunct_tokenize

import sys  



reload(sys)  
sys.setdefaultencoding('utf8')
reload(sys)
def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x


with open("my_dict.json") as f:
	my_dict_trigrams = json.load(f)



with open("bigrams.json") as f:
	my_dict_bigrams = json.load(f)


lll = len(my_dict_bigrams)*0.0000140785583556
minim = 1
c = 0

# with open("prob_val.json") as f:
my_dict_prob = {}
for i in my_dict_trigrams:
	#for j in range(len(i)):
	#	if(i[len(i)-1-j] == " " ):
	#		val = len(i)-1-j
	#		break
	new = i.split()
	#print new

	bi = new[0] + " " + new[1]
	

	my_dict_prob[i] = (int(my_dict_trigrams[i])*1.0 + 1*0.0000140785583556)/(int(my_dict_bigrams.get(bi , 0)) + lll )


	minim = min(my_dict_prob[i] , minim)	

lll = len(my_dict_bigrams)*0.0000140785583556

fh = open("mytestdb.txt","r+")

test_data = fh.read()

final_test_data = ""


for i in test_data:
	if(ord(i)>=128):
		continue
	else:
		final_test_data += i


arr = my_dict_prob.keys()
arr.sort()


def calc_prob(sen,my_dict_prob , lll, my_dict_bigrams):
	myprob = 1
	newsen = wordpunct_tokenize(sen)
	new2 = trigrams(newsen)
	if(len(newsen)>50):
		print sen
		print ""

	for i in new2:
		triitself = i[0] + " " + i[1] + " "+i[2]
		# if(binary_search(arr , triitself)):
		# 	print "It is present"
		# else:
		# 	print "Na"
		bii =  i[0] + " " + i[1]
		myprob *= my_dict_prob.get(triitself , 0.0000140785583556/(lll+int(my_dict_bigrams.get(bii , 0))))
	return (myprob , len(newsen))


sentences = sent_tokenize(final_test_data.lower())
wrong_data = sent_tokenize((final_test_data.lower())[::-1])
probablities = {}
prob2 = []

for i in sentences:
	val,ll = calc_prob(i, my_dict_prob , lll , my_dict_bigrams)
	if( ll not in probablities):
		probablities[ll] = []
	probablities[ll].append(val)


fh = open("test2.txt","r+")
test_data = fh.read()
final_test_data = ""
for i in test_data:
	if(ord(i)>=128):
		continue
	else:
		final_test_data += i

sentences = sent_tokenize(final_test_data.lower())

for i in sentences:
	val,ll = calc_prob(i, my_dict_prob , lll , my_dict_bigrams)
	if( ll not in probablities):
		probablities[ll] = []
	probablities[ll].append(val)

fh = open("test3.txt","r+")
test_data = fh.read()
final_test_data = ""
for i in test_data:
	if(ord(i)>=128):
		continue
	else:
		final_test_data += i

sentences = sent_tokenize(final_test_data.lower())

for i in sentences:
	val,ll = calc_prob(i, my_dict_prob , lll , my_dict_bigrams)
	if( ll not in probablities):
		probablities[ll] = []
	probablities[ll].append(val)

fh = open("test4.txt","r+")
test_data = fh.read()
final_test_data = ""
for i in test_data:
	if(ord(i)>=128):
		continue
	else:
		final_test_data += i

sentences = sent_tokenize(final_test_data.lower())

for i in sentences:
	val,ll = calc_prob(i, my_dict_prob , lll , my_dict_bigrams)
	if( ll not in probablities):
		probablities[ll] = []
	probablities[ll].append(val)

fh = open("test5.txt","r+")
test_data = fh.read()
final_test_data = ""
for i in test_data:
	if(ord(i)>=128):
		continue
	else:
		final_test_data += i

sentences = sent_tokenize(final_test_data.lower())

for i in sentences:
	val,ll = calc_prob(i, my_dict_prob , lll , my_dict_bigrams)
	if( ll not in probablities):
		probablities[ll] = []
	probablities[ll].append(val)


newarr = probablities.keys()
newarr.sort()
for i in newarr:
	probablities[i].sort()
	print "The length of sentence under consideration is " , i
	print "The average of probabilities of these sentences is ", (sum(probablities[i])*1.0)/len(probablities[i])
	print "Val of first quarter" , sum(probablities[i][:len(probablities[i])/4])/len(probablities[i])/4
	print "Val of 1/3" , sum(probablities[i][:len(probablities[i])/3])/len(probablities[i])/3
	print "Val of 3/4" , sum(probablities[i][:3*(len(probablities[i]))/4])/(3*len(probablities[i])/4)
	print "Val of 1/2" , sum(probablities[i][:len(probablities[i])/2])/len(probablities[i])/2


# print "Minimum" , min(probablities)
# print "Maximum" , max(probablities)
# print "Average of probablities" , sum(probablities)/len(probablities)

# print "Minimum" , min(prob2)
# print "Maximum" , max(prob2)
# print "Average of probablities" , sum(prob2)/len(prob2)