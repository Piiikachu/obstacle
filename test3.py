import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from myconsts import *


def join_filename(type, pos):
    return '3-%d-%s.csv' % (type, pos)


def read_df(df):
    # todo: add more
    x = np.array(df['Points:0'])
    u = np.array(df['f_1[4]'])
    v = np.array(df['f_1[5]'])

    #normalize
    xn=x/0.04515
    un=u/U_INF
    vn=v/U_INF

    return xn,un,vn

def join_label(t):
    return r"$L/H=%s$"%labels[t]

types = [3, 6, 12]
positions = ['0.25', '0.5', '0.75']
labels={3:'1',6:'1/2',12:'1/4'}
dfs = []
figs = []
i= 0
for pos in positions:
    for t in types:
        df = pd.read_csv(join_filename(t, pos))
        x, u, v = read_df(df)
        plt.figure(10*i)
        plt.plot(x,u,label=join_label(t))
        plt.xlabel(r'$Dimensionless\ Length\ X$')
        plt.ylabel(r'$Tangential\ Velocity\ Ratio\ (u/U_\infty)$')
        plt.legend(loc='best')
        plt.grid()

        plt.figure(10*i+1)
        plt.plot(x, v, label=join_label(t))
        plt.xlabel(r'$Dimensionless\ Length\ X$')
        plt.ylabel(r'$Normal\ Velocity\ Ratio\ (v/U_\infty)$')
        plt.legend()
        plt.grid()


    i += 1

plt.show()