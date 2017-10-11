---
---
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1)

a = -2

x1 = x + (x - np.exp(a) * np.exp(x)) / (x-1)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x, x1)

ax.plot(x,x)
ax.plot(x,x*0)

ax.set_ylim(-1,1)

fn = "/home/crymal/temp/test.svg"

plt.savefig(fn)
with open(fn) as f:
    print(f.read())

