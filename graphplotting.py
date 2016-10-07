import matplotlib.pylab as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
print style.available
#style.use("gg_plot")
x,y = np.loadtxt('example.csv',dtype='float',unpack='True' , delimiter=',')
plt.plot(x  , y ,label = 'line1', linewidth = 2)
plt.title("My first graph plotted" , size = '15' )
plt.xlabel('Time')
plt.xscale('log')
plt.ylabel('Velocity')
plt.legend()
plt.show()



