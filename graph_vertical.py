import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from    scipy.signal import savgol_filter
LAMBDA=0.0009


def plot_smooth_xy(df,x,y,label):
    x = np.array(df[x])
    v = np.array(df[y])
    v_smooth = savgol_filter(v, 51, 3)
    plt.plot(v_smooth, x / LAMBDA, label=label)

def plot_smooth(df,label):
    x=np.array(df['Points:1'])
    v=np.array(df['f_1[5]'])
    v_smooth=savgol_filter(v,51,3)
    plt.plot(v_smooth,x/LAMBDA,label=label)

df1=pd.read_csv('3-6-41.csv')
df2=pd.read_csv('3-6-43.csv')
df3=pd.read_csv('3-6-45.csv')

plt.figure()

plot_smooth(df1,'41mm')
plot_smooth(df2,'43mm')
plot_smooth(df3,'45mm')
# plot(df1,'41')
# plot(df2,'43')
# plot(df3,'45')
plt.ylabel(r'$mean\ free\ path\ \lambda$')
plt.xlabel('normal velocity')
plt.legend(loc='best')

plt.figure()
plot_smooth_xy(df1,'Points:1','f_1[4]','41mm')
plot_smooth_xy(df2,'Points:1','f_1[4]','43mm')
plot_smooth_xy(df3,'Points:1','f_1[4]','45mm')

plt.ylabel(r'$mean\ free\ path\ \lambda$')
plt.xlabel('tangential velocity')
plt.legend(loc='best')
plt.show()
