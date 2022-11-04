#Matplotlib

#Simple Plot
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5], [1,4,9,16], 'b.')
plt.ylabel ('numbers')
plt.show

#Two Dimensional plot
import numpy as np

x = np.arrange(0.0, 10.0, 0.01)
y = 3.0 * x
noise = np.random.normal(0.0, 1.0, len (x))

plt.plot(x,y,'b.', label = "Expected Data")
plt.plot(x, y + noise , 'g-', label = 'Actual Data')

#Adding labels and legends

plt.title ('create plot')
plt.xlabel('Average speed (km per hour)')
plt.ylabel('Distance Covered (km)')
plt.legend()

#Histogram 
x = np.random.normal(0.0, 1.0, 100000.0)
plt.hist(x, bins=20)
plt.show

#Side by side plots
x = np.random.normal (0.0, 1.0, 10000)
plt.subplot(1,2,1)
plt.hist(x, bins =80)

x = np.random.uniform(-4.0, 3.0, 10000)
plt.subplot(1, 2, 2)
plt.hist(x)

plt.show()

#Other plots

