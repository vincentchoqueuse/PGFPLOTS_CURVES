
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lg

from scipy.signal import lti

# create system
K=1
m=0.5
wn=1
system=lti([K],[(1/(wn**2)),2*m/wn,1])

t,s=system.step()
w, mag, phase = system.bode()

plt.figure()
plt.plot(t,s)
plt.figure()
plt.semilogx(w, mag)

step_data=np.transpose([np.ravel(t),np.ravel(s)])
np.savetxt("step_response.csv", step_data, delimiter=",")   #export file

bode_data=np.transpose([np.ravel(w),np.ravel(mag),np.ravel(phase)])
np.savetxt("bode_diagram.csv", bode_data, delimiter=",")   #export file

plt.show()