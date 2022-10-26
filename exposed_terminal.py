# Calculate the prob an exposed terminal.


import random
import numpy as np
from matplotlib import pyplot as plt

r = 10000 # coverage of the node
PA = []
repeat_simulations = 10000

# pick cords 0,0 for Node-A
for each in range (repeat_simulations):

    ## Next, we pick cords for Node-B.
        #pick random angle for Node-B w.r.t (0,0)
    B_angle = random.uniform (-np.pi,np.pi)
    #print ("B_angle " + str (B_angle))

    #Place Node-B a random distance away from Node-A but within range r of Node-A. 
    B_amplitude =  random.uniform (0,0.99*r)
    #print ("B_amplitude " + str (B_amplitude))

    # Calculate the distance between Node-A at (0,0) and Node-B.
    dist_bet_centrs = np.sqrt((B_amplitude * np.cos(B_angle))**2 + (B_amplitude * np.sin(B_angle))**2)
    #print ("dist_bet_centrs " + str (dist_bet_centrs))

    # Calculate the common coverage area for Node-A,B.
    # https://mathworld.wolfram.com/Circle-CircleIntersection.html
    # https://math.stackexchange.com/questions/97850/get-the-size-of-an-area-defined-by-2-overlapping-circles
    # https://diego.assencio.com/?index=8d6ca3d82151bad815f78addf9b5c1c6
    common_area = (r**2) * np.arccos(dist_bet_centrs/(2 * r)) + r**2 * np.arccos(dist_bet_centrs/(2 * r))  \
        - 0.5 * np.sqrt( (2*r-dist_bet_centrs)* dist_bet_centrs * dist_bet_centrs * (2*r+dist_bet_centrs) )
    
    #  Exclusive area attributing to a single node's coverage.
    exclusive_area = (np.pi * r**2 ) - common_area

    # Compute prob of exposed terminal interms of converage areas.
    PA.append ( ( exclusive_area**2) / ((np.pi * r**2 )**2 ) )

#convert prob to percentages
PA = [i * 100 for i in PA]

#PLOT
#plt.hist(PA, bins=100, range=[0,100],facecolor='gray', align='mid')
plt.hist(PA,bins=100)
plt.title("Probability Histogram of Exposed Terminal Occurrences")
plt.ylabel('Occurrences Per 10K')
plt.xlabel('Probability (%)')
plt.show()
