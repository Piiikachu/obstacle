import pandas as pd

columns=['id','c1','c2','n','nrho','massrho','u','v','temp','trot','tvib','temp','press','xlo','ylo','xhi','yhi']
df=pd.read_csv('tmp_flow.90000',sep=' ')
# df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
df=df.drop(['Unnamed: 17'],axis=1)
df.columns=columns
df=df.apply(pd.to_numeric,errors='ignore')

def header(f):
    TITLE='Simple Data File'
    VARIABLES=['X','Y']
    ZONE={'I':4} 
    DATAPACKING='POINT'
    # 1 1
    # 2 1
    # 2 2
    # 1 2
    # TEXT X=10 Y=90 T="Simple Text"

    f.write('TITLE="%s"\n'%TITLE)
    f.write('VARIABLES="'+str(VARIABLES))

with open('flow.dat','w') as f:
    header(f)
    pass

print(df.info())
    