import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

def plot_smooth(df):
    x=np.array(df['Points:1'])
    v=np.array(df['f_1[5]'])
    v_smooth=savgol_filter(v,51,3)
    return x,v_smooth

if __name__ == '__main__':
    df = pd.read_csv('3-6-45.csv')
    plot_smooth(df)