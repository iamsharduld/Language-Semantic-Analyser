#!/usr/bin/env python
import math
import matplotlib
import json
matplotlib.use('TkAgg')

from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.tokenize import wordpunct_tokenize
from nltk import bigrams,trigrams
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

from matplotlib import style

from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


global my_dict_trigrams,my_dict_bigrams, my_dict_prob

global a

with open("my_dict.json") as f:
    my_dict_trigrams = json.load(f)

with open("bigrams.json") as f:
    my_dict_bigrams = json.load(f)


#Probabilities array
global lll
lll = len(my_dict_bigrams)*0.0000140785583556
minim = 1
c = 0

# with open("prob_val.json") as f:
my_dict_prob = {}
for i in my_dict_trigrams:
    #for j in range(len(i)):
    #   if(i[len(i)-1-j] == " " ):
    #       val = len(i)-1-j
    #       break
    new = i.split()
    #print new

    bi = new[0] + " " + new[1]
    

    my_dict_prob[i] = (int(my_dict_trigrams[i])*1.0 + 1*0.0000140785583556)/(int(my_dict_bigrams.get(bi , 0)) + lll )


    minim = min(my_dict_prob[i] , minim)    


def calc_prob(sen,my_dict_prob , lll, my_dict_bigrams,a):
    myprob = 1
    newsen = wordpunct_tokenize(sen)
    new2 = trigrams(newsen)
    arr1 = []
    arr2 = []
    count = 3   
    for i in new2:
        triitself = i[0] + " " + i[1] + " "+i[2]        
        bii =  i[0] + " " + i[1]
        myprob *= (my_dict_prob.get(triitself , 0.0000140785583556/(lll+int(my_dict_bigrams.get(bii , 0)))))
        arr1.append(count)
        arr2.append(math.log10(myprob))
        count+=1
    return arr1, arr2

    #return myprob




root = Tk.Tk()
root.wm_title("Probabilty Calculator of English Sentences")

style.use("ggplot")
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
plt.xlabel("Number of words ")
plt.ylabel("Probabilty in Log to the base 10 ")


t = [3,4,5,6,7,8,9,10,11,12,13,14,15]

s = [0.0374353327642,0.00114531566828,0.000188340824791,1.73746755198e-06,8.64489973985e-08,2.56563268524e-09,9.53126238061e-12,2.04966389569e-13,6.35537935433e-15,3.53289759783e-18,2.67720293565e-18,2.58654344825e-22,2.58540636076e-27]
avgquar = [5.34684044538e-07,8.20610060456e-14,6.26709972464e-20,1.15033664528e-25,4.0651855757e-30,2.45764269373e-35,9.91400286239e-41,7.04395632008e-46,1.14725544058e-50,1.34718078665e-55,1.31733672494e-60,8.12102932419e-66,1.40213337415e-71]
avgthird = [6.61978735349e-08,1.62521590208e-14,1.42448306264e-20,2.14870754876e-24,5.1756900997e-30,2.36067269933e-35,3.2416599902e-39,6.40921470622e-45,9.0522655651e-50,4.94167229884e-54,1.95633366682e-59,8.57764813154e-65,3.51683192408e-69]
avg34 = [0.00401870277685,3.35274606265e-09,4.0278147938e-13,3.45584656193e-17,.22712720263e-20,3.42398754826e-25,5.8732823803e-29,4.57573325934e-34,8.99480674914e-37,1.40784829545e-41,1.32359780491e-45,3.23083515804e-50,3.29985107988e-54]

snew = []
#log 
for i in avg34:
    snew.append(math.log10(i))

#f = plt.plot(t,s)
a.plot(t,snew, c = 'g')
plt.yscale('log')
v = "The default value"
e = Tk.Entry(master = root , textvariable = v)
e.pack(side = Tk.BOTTOM)
s = e.get()
e.focus_set()
print s

def callback():
    x = e.get()     #This is printed in terminal
    '''print x
    print "1"
    if(x=="1"):
        va = 5
        print "yo1"
    elif(x=="2"):
        va = 15
        print "yo2"
    else:
        va = 10
        print "yo3"'''
    global a
   # a.plot([i for i in range(va)],[i for i in range(va)])
    if(x!=""):
       one , two = calc_prob(x.lower(), my_dict_prob , lll , my_dict_bigrams,a)
       print one,two
       a.plot(one,two)







b2 = Tk.Button(master = root, text="get", width=10, command=callback)
b2.pack(side = Tk.BOTTOM )#, x = 100 , y = 100)
b2.pack(padx = 2 , pady = 2)




# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
