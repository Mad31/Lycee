# LFT 2018 test
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

xmin, ymin, xmax, ymax = -0.2, -0.1, 0.2, 0.1

h = .0005
X = np.arange(xmin, xmax, h)
Y = np.arange(ymin, ymax, h)
X0=[-0.1,0.1,0]
Y0=[0,0,0.05]
Rlim=0.00001

XX,YY = np.meshgrid(X, Y)

R1=np.sqrt((XX+0.1)**2+YY**2)
# R1[R1**2<Rlim] = np.nan 
V1=1/R1

R2=np.sqrt((XX-0.1)**2+YY**2)
# R2[R2**2<Rlim] = np.nan 
V2=1/R2

R3=np.sqrt((XX)**2+((YY-0.05)**2))
# R2[R2**2<Rlim] = np.nan 
V3=1/R3

V=V1+V2+V3
plt.axis('equal')
niveau=np.logspace(1,3, num= 50)
print(niveau)

plt.scatter(XX,YY,s=2,c="black")
plt.scatter(X0,Y0,s=20,c='blue')
C= plt.contourf(XX, YY, V, niveau ,norm = LogNorm())
# C= plt.contourf(XX, YY, V, niveau , norm = LogNorm())
plt.colorbar(C)
# plt.contour(XX, YY, V, niveau, colors='black', linewidth=.1)
plt.show()
