#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import sys

loamTrajectory = np.loadtxt(sys.argv[1])
plt.plot(loamTrajectory[:,1],loamTrajectory[:,2])
plt.show()
