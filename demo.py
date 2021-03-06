import numpy as np
import kappalib as kp
from scipy.stats import t

n = 12

np.random.seed(123)

x = np.random.randn(n)
y = x + 2

with open('random.csv', 'w') as f:
    for j,i in zip(np.r_[['A'],x],np.r_[['B'],y]):
        f.write(str(j)+','+str(i)+'\n')

n1 = np.size(x) # Number of elements in sample 1
n2 = np.size(y) # Number of elements in sample 2
v = n1 + n2 - 2 # Degrees of Freedom
                
s1 = np.var(x, ddof=1) # Variance of sample 1 
s2 = np.var(y, ddof=1) # Variance of sample 2 
                
sp =  kp.stats.pooledVar(x,y) # Pooled Variance
                                
df = np.mean(x) - np.mean(y) # Difference
denom = np.sqrt(sp*(1/n1+1/n2)) # Standart Error

with np.errstate(divide='ignore', invalid='ignore'):
    statistic = np.divide(df, denom) # Statistic




# Two Sample t-test

# data:  x and y
# t = -28.779, df = 198, p-value < 2.2e-16
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#  -4.274093 -3.725907
# sample estimates:
# mean of x mean of y 
# 0.1908471 4.1908471 

