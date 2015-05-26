import matplotlib.pyplot as plt
import numpy as np

length = np.random.random(10)
length.sort()
time = range(1,11)
# time.sort()

print("Length: %s" % length)
print("Time: %s" % time)
slope, intercept = np.polyfit(time, length, 1)
print(slope)
plt.plot(time, length, '--')
plt.show()
