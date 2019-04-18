import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Pressure_INF = 5.582
Density_INF = 8.753e-5
Velocity_INF = 7456


def pressure_co(df):
    return (df['f_2[2]'] - Pressure_INF) / (Velocity_INF ** 2 * Density_INF / 2)


def heat_flux(df):
    return df['f_2[7]'] / (Velocity_INF ** 3 * Density_INF / 2)


def skin_friction_co(df,horizon):
    if  horizon:
        return df['f_2[5]']/ (Velocity_INF ** 2 * Density_INF / 2)
    else:
        return df['f_2[6]']/ (Velocity_INF ** 2 * Density_INF / 2)



def join_file_name(name):
    return name + ".surf"


def get_label():
    return r'$L/H=$' + labellist[i]


def plot_hco(vx, vy, hco):
    plt.figure(1)
    plt.plot(vx, hco, label=get_label())
    plt.xlabel("vx")
    plt.ylabel("Heat flux co")
    plt.legend(loc='best')
    plt.grid()


def plot_fsh(vx, vy, fsh):
    plt.figure(3)
    plt.plot(vx, fsh, label=get_label())
    plt.xlabel("vx")
    plt.ylabel("Skin Friction co")
    plt.legend(loc='best')
    plt.grid()


def plot_pco(vx, vy, pco):
    plt.figure(2)
    plt.plot(vx, pco, label=get_label())
    plt.xlabel("vx")
    plt.ylabel("Pressure co")
    plt.legend(loc='best')
    plt.grid()


def plot_surf(surf, horizon):
    vx, vy, pco, hco, fshear = getdata(surf, horizon)
    plot_hco(vx, vy, hco)
    plot_fsh(vx, vy, fshear)
    plot_pco(vx, vy, pco)


def seprate_surf(surfs, dfsort):
    dfsurf = []
    for i in range(5):
        j = i + 1
        dfsurf.append(dfsort[surfs[i]:surfs[j]])
    return dfsurf


def getdata(df, horizon):
    vx = (np.array(df['v1x']) + np.array(df['v2x'])) / 2
    vy = (np.array(df['v1y']) + np.array(df['v2y'])) / 2
    pco = np.array(pressure_co(df))
    heatco = np.array(heat_flux(df))
    # todo: normalize shear force
    fshear=np.array(skin_friction_co(df,horizon))
    return vx, vy, pco, heatco, fshear


# 文档名
groups = ['3-3', '3-6', '3-12']
dfs = []

# 面节点
surf3 = [0, 75, 105, 120, 135, 199]
surf6 = [0, 79, 109, 124, 154, 271]
surf12 = [0, 79, 139, 154, 214, 330]

dfdic = {}
surfdic = {'3-3': surf3, '3-6': surf6, '3-12': surf12}
surflist = [surf3, surf6, surf12]

labellist = ['1', '1/2', '1/4']

fig_hco = plt.figure(1)
fig_pco = plt.figure(2)
fig_fsh = plt.figure(3)

i = 0

for name in groups:
    df = pd.read_csv(join_file_name(name), sep=' ')
    dfs.append(df)
    # dfdic.update({df: name})

for df in dfs:
    surfs = surflist[i]
    dfsort = df.sort_values(by='SURFS_id')

    dfsurf = seprate_surf(surfs, dfsort)
    # for surf in dfsurf:
    s1 = dfsurf[0]
    plot_surf(s1, True)
    i += 1

plt.show()
# print(dfsort.iloc[79])
# var_list_hor = ['f_2[2]', 'f_2[7]', 'f_2[5]']
# var_list_ver = ['f_2[2]', 'f_2[7]', 'f_2[6]']

# var_normal = {'f_2[2]': pressure_co(), }
