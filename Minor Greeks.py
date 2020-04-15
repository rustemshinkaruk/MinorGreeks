import numpy as np
import math 
import matplotlib.pyplot as plt
from scipy.stats import norm

K=100
S=np.arange(70,130,5)
r=0.02
sig=0.2
t=2

def call(S,K,r,sig,t):
    d1=(np.log(S/K)+(r+sig**2/2)*t)/(sig*math.sqrt(t))
    d2=d1-sig*math.sqrt(t)
    c=S*norm.cdf(d1)-K*math.exp(-r*t)*norm.cdf(d2)
    return(c)

c=np.array(call(S,K,r,sig,t))
d1=(np.log(S/K)+(r+sig**2/2)*t)/(sig*math.sqrt(t))
d2=d1-sig*math.sqrt(t)


lambd=(S/c)*norm.cdf(d1)# in percentages

vega=S*np.sqrt(t)*norm.pdf(d1)
rho=K*t*math.exp(-r*t)*norm.cdf(d2)
theta=-S*norm.pdf(d1)*sig/(2*math.sqrt(t))-r*rho/t

dl_dc=S*norm.cdf(d1)/(-c**2)
dl_dsig=dl_dc*vega
dl_dr=dl_dc*rho
dl_dt=dl_dc*theta


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#fig.suptitle('Lambda derivatives plots')
ax1.plot(S, lambd)
ax1.set_title('Leverage over different Stock values', fontsize=8)
ax1.set(xlabel='Stock Price in $', ylabel='Leverage in %')
ax1.set_ylim([3,8])

ax2.plot(S,dl_dsig)
ax2.set_title('Sensitivity of Leverage to volatility', fontsize=8)
ax2.set(xlabel='Stock Price in $', ylabel='Leverage change in %')


ax3.plot(S,dl_dt)
ax3.set_title('Sensitivity of Leverage to Time', fontsize=9)
ax3.set(xlabel='Stock Price in $', ylabel='Leverage change in %')

ax4.plot(S,dl_dr)
ax4.set_title('Sensitivity of Leverage to risk-free rate', fontsize=8)
ax4.set(xlabel='Stock Price in $', ylabel='Leverage change in %')



fig.tight_layout(pad=1.0)


