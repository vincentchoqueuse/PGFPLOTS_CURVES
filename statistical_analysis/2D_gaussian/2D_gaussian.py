#!/Users/choqueuse/anaconda/bin/python

from scipy.stats import multivariate_normal
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import scipy.linalg as lg


path="gaussian"
Cov=np.matrix([[2,0.5],[0.5,0.7]])

tauz=Cov[0,0]-Cov[1,1]+2j*Cov[1,0]
sigmaz=Cov[0,0]+Cov[1,1]

lambda1=(sigmaz+np.abs(tauz))/2
lambda2=(sigmaz-np.abs(tauz))/2
alpha=np.angle(tauz)/2

e1=np.array([np.cos(alpha),np.sin(alpha)])
e2=np.array([-np.sin(alpha),np.cos(alpha)])

x, y = np.mgrid[-5:5:.25, -5:5:.25]
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x; pos[:, :, 1] = y
rv = multivariate_normal([0,0],Cov)
z= rv.pdf(pos)

plt.contourf(x, y,z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y, rv.pdf(pos),cmap='hot', rstride=1, cstride=1,linewidth=0, antialiased=False)
data=np.transpose([np.ravel(x),np.ravel(y),np.ravel(z)])
np.savetxt("2D_gaussian.csv", data, delimiter=",")   #export file


plt.show()


