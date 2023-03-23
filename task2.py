# Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import math
import numpy as np
from scipy import stats

x=np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
xmean=np.mean(x)                                  # среднее арифметическое для выборки x
print(xmean)
D=np.var(x,ddof=1)                                # несмещенная дисперсия для выборки x
print(D)
t=stats.t.ppf(0.975,len(x)-1)                     # коэффициент Стьюдента
print(t)
a=xmean-t*np.sqrt(D/len(x)) 
b=xmean+t*np.sqrt(D/len(x))        
print(f'Доверительный интервал: {[a , b]}')