# This code mkaes two normally distributed curve
# import numpy
import numpy as np
#import matplotlib pyplot
import matplotlib.pyplot as plt
#import norm from scipy
from scipy.stats import norm
# if you want change the deaful font settings, use the next three line
# I will modify each text therefore, I will not use this.
#plt.rcParams['font.size'] = '20' # set default font size to 20
#plt.rcParams["font.family"] = 'Arial' # set default font to Arial
#plt.rcParams['font.style'] = 'normal' # Set default style to normal
# make normally distibuted data 
x= np.arange (-5, 7, 0.001)
y= np.arange (-5, 7, 0.001)
# define plot settings
fig, ax = plt.subplots()
# Set axis to top and bottom only
ax.spines[['right', 'top']].set_visible(False)
# plot first curve (let say low flow) starting from 2.1 and interval 1.5
plt.plot(x, norm.pdf(x, 2.1, 1.5))
         #, label="Low flow")
#plot second curve (let say high flow)
plt.plot(y, norm.pdf(y, 2.5, 1.5))
         #, label= 'High flow')
# plot legends with font size 17, position upper left corner
#plt.legend(["Low Flow", "High Flow"], fontsize="17", loc ="upper left")
# Omit tick marks on axis
plt.tick_params(labelleft=False, left=False)
plt.tick_params(labelbottom=False, bottom=False)
# plot x and y axis level,  font size 28
#plt.ylabel('Fraction (%)', fontsize=28)
#plt.xlabel('Diameter (µm)', fontsize=28)
# get the legend object
leg = ax.legend()
# change the line width for the legend
#for line in leg.get_lines():
   # line.set_linewidth(2.0)
#plt.legend(["Low Flow", "High Flow"], fontsize="27.5", loc = "upper left", handlelength=0.5, handletextpad=0.1, frameon=False)
#plt.xlim([-5, 5])
#plt.savefig('figure5a.pdf')
plt.show()


# In[ ]:




