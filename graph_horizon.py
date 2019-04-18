import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from    scipy.signal import savgol_filter
LAMBDA=0.0009


def plot_smooth_xy(df,x,y,label):
    x = np.array(df[x])
    v = np.array(df[y])
    v_smooth = savgol_filter(v, 51, 3)
    plt.plot(x / LAMBDA,v_smooth, label=label)

def plot_smooth(df,label):
    x=np.array(df['Points:0'])
    v=np.array(df['f_1[5]'])
    v_smooth=savgol_filter(v,51,3)
    plt.plot(x / LAMBDA,v_smooth, label=label)
df1=pd.read_csv('3-6-1.csv')
df2=pd.read_csv('3-6-3.csv')
df3=pd.read_csv('3-6-5.csv')

plt.figure()

plot_smooth(df1,'1mm')
plot_smooth(df2,'3mm')
plot_smooth(df3,'5mm')
# plot(df1,'41')
# plot(df2,'43')
# plot(df3,'45')
plt.xlabel(r'$mean\ free\ path\ \lambda$')
plt.ylabel('normal velocity')
plt.legend(loc='best')

plt.figure()
plot_smooth_xy(df1,'Points:0','f_1[4]','1mm')
plot_smooth_xy(df2,'Points:0','f_1[4]','3mm')
plot_smooth_xy(df3,'Points:0','f_1[4]','5mm')

plt.xlabel(r'$mean\ free\ path\ \lambda$')
plt.ylabel('tangential velocity')
plt.legend(loc='best')
plt.show()