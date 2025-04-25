name: str='dr.ardestani---alireza-panahi'
print(f'{name:_^50}')
# ----------------------------------------------------------
import math 
import numpy 
# تابع توزیع گوسی
def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2.0 * math.pi)
#تابع توزیع گوسی با میو و سیگما
def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma
#دو تابع بالا سر کلاس گفته شد
# تابع تجمعی گوسی
def cdf(x,mu=0.0,sigma=1.0,t=40):
    # محاسبه فی زد
    z = (x - mu) / sigma
    phi_z = phi(z)
    sum = 0
    den = 1
    for n in range(t):
        t = (z ** (2 * n + 1)) / den
        sum += t
        den *= (2 * n + 3)    
    # محاسبه CDF
    cdf = 0.5 + phi_z * sum
    return cdf