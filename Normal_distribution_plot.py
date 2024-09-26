# This code mkaes two normally distributed curve
# We appreciate your citation of this article if you use this code: 
# Hefzul Bari, S., Yokoo, Y., & Leong, C. (2024). A brief review of recent global trends in suspended sediment estimation studies. Hydrological Research Letters, 18(2), 51–57. 
# https://doi.org/10.3178/hrl.18.51
# import numpy
import numpy as np
#import matplotlib pyplot
import matplotlib.pyplot as plt
#import norm from scipy
from scipy.stats import norm

# make normally distibuted data 
x= np.arange (-5, 7, 0.001)
y= np.arange (-5, 7, 0.001)
# define plot settings
fig, ax = plt.subplots()
# Set axis to top and bottom only
ax.spines[['right', 'top']].set_visible(False)
# plot first curve (let say low flow) starting from 2.1 and interval 1.5
plt.plot(x, norm.pdf(x, 1.90, 1.5))
         #, label="Low flow")
#plot second curve (let say high flow)
plt.plot(y, norm.pdf(y, 3.2, 1.5))
         #, label= 'High flow')
# plot legends with font size 17, position upper left corner
#plt.legend(["Low Flow", "High Flow"], fontsize="17", loc ="upper left")
# Omit tick marks on axis
plt.tick_params(labelleft=False, left=False)
plt.tick_params(labelbottom=False, bottom=False)
# plot x and y axis level,  font size 28
plt.ylabel('Fraction (%)', fontsize=28)
plt.xlabel('Diameter (µm)', fontsize=28)
# get the legend object
leg = ax.legend()
# change the line width for the legend
#for line in leg.get_lines():
   # line.set_linewidth(2.0)
#plt.legend(["Low Flow", "High Flow"], fontsize="27", loc = "upper left", handlelength=0.5, handletextpad=0.1, frameon=False)
plt.legend(["Low Flow", "High Flow"], fontsize="27", loc = "upper left", bbox_to_anchor=(-0.05, 1), handlelength=0.5, handletextpad=0.1, frameon=False)
#plt.xlim([-5, 5])
plt.show()



